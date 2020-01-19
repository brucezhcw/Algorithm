
////////////////////////////////////////////////////////////////////////////////

#define Kp 10.0f                          // 这里的Kp Ki是用于调整加速度计修正陀螺仪的速度
#define Ki 0.008f                        
#define halfT 0.001f                      // 采样周期的一半，用于求解四元数微分方程时计算角增量

float q0 = 1, q1 = 0, q2 = 0, q3 = 0;     // 初始姿态四元数
float exInt = 0, eyInt = 0, ezInt = 0;    //当前加计测得的重力加速度在三轴上的分量

//与用当前姿态计算得来的重力在三轴上的分量的误差的积分
void IMUupdate(float gx, float gy, float gz, float ax, float ay, float az)   //g表陀螺仪，   a表加速度计
{
    float q0temp,q1temp,q2temp,q3temp;//四元数暂存变量，求解微分方程时要用
    float norm; //矢量的模或四元数的范数
    float vx, vy, vz;//当前姿态计算得来的重力在三轴上的分量
    float ex, ey, ez;//当前加计测得的重力加速度在三轴上的分量
    //与用当前姿态计算得来的重力在三轴上的分量的误差

    float q0q0 = q0*q0;
    float q0q1 = q0*q1;
    float q0q2 = q0*q2;
    float q1q1 = q1*q1;
    float q1q3 = q1*q3;
    float q2q2 = q2*q2;
    float q2q3 = q2*q3;
    float q3q3 = q3*q3;

    if(ax*ay*az < 1e-6 && ax*ay*az > -1e-6)//加计处于自由落体状态时不进行姿态解算，因为会产生分母无穷大的情况
            return;

    norm = sqrt(ax*ax + ay*ay + az*az);//单位化加速度计，
    ax = ax / norm;// 这样变更了量程也不需要修改KP参数，因为这里归一化了
    ay = ay / norm;
    az = az / norm;

    //用当前姿态计算出重力在三个轴上的分量，
    vx = 2*(q1q3 - q0q2);
    vy = 2*(q0q1 + q2q3);
    vz = q0q0 - q1q1 - q2q2 + q3q3 ;

    //计算测得的重力与计算得重力间的误差，向量外积可以表示这一误差
    ex = (ay*vz - az*vy) ;                                                                  
    ey = (az*vx - ax*vz) ;
    ez = (ax*vy - ay*vx) ;

    exInt = exInt + ex * Ki;                                           //对误差进行积分
    eyInt = eyInt + ey * Ki;
    ezInt = ezInt + ez * Ki;

    // 调整陀螺仪观测数据
    gx = gx + Kp*ex + exInt;    //将误差PI后补偿到陀螺仪，即补偿零点漂移
    gy = gy + Kp*ey + eyInt;
    gz = gz + Kp*ez + ezInt;    //这里的gz由于没有观测者进行矫正会产生漂移，表现出来的就是积分自增或自减

    //下面进行姿态的更新，也就是四元数微分方程的求解
    q0temp=q0;//暂存当前值用于计算
    q1temp=q1;//网上传的这份算法大多没有注意这个问题，在此补上
    q2temp=q2;
    q3temp=q3;

    //采用一阶毕卡解法
    q0 = q0temp + (-q1temp*gx - q2temp*gy -q3temp*gz)*halfT;
    q1 = q1temp + (q0temp*gx + q2temp*gz -q3temp*gy)*halfT;
    q2 = q2temp + (q0temp*gy - q1temp*gz +q3temp*gx)*halfT;
    q3 = q3temp + (q0temp*gz + q1temp*gy -q2temp*gx)*halfT;

    //单位化四元数在空间旋转时不会拉伸，仅有旋转角度，这类似线性代数里的正交变换
    norm = sqrt(q0*q0 + q1*q1 + q2*q2 + q3*q3);
    q0 = q0 / norm;
    q1 = q1 / norm;
    q2 = q2 / norm;
    q3 = q3 / norm;

    //四元数到欧拉角的转换
    Q_ANGLE.Z = GYRO_I.Z; // yaw
    Q_ANGLE.Y = asin(-2 * q1 * q3 + 2 * q0* q2)*57.3; // pitch
    Q_ANGLE.X = atan2(2 * q2 * q3 + 2 * q0 * q1,-2 * q1 * q1 - 2 * q2* q2 + 1)* 57.3; // roll
}
