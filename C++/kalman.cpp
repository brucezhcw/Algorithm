/*
	假设我们要研究的对象是一个房间的温度。根据你的经验判断，这个房间的温度是恒定的，
也就是下一分钟的温度等于现在这一分钟的温度（假设我们用一分钟来做时 间单位）。假设你
对你的经验不是100%的相信，可能会有上下偏差几度。我们把这些偏差看成是高斯白噪声，也
就是这些偏差跟前后时间是没有关系的而且符合高斯分配。另外，我们在房间里放一个温度计，
但是这个温度计也不准确的，测量值会比实际值偏差。我们也把这些偏差看成是高斯白噪声。       
好了，现在对于某一分钟我们有两个有关于该房间的温度值：你根据经验的预测值（系统的预测值）
和温度计的值（测量值）。下面我们要用这两个值结合他们各自的噪声来估算出房间的实际温度值。       
假 如我们要估算k时刻的是实际温度值。首先你要根据k-1时刻的温度值，来预测k时刻的温度。
因为你相信温度是恒定的，所以你会得到k时刻的温度预测值是跟 k-1时刻一样的，假设是23度，
同时该值的高斯噪声的偏差是5度（5是这样得到的：如果k-1时刻估算出的最优温度值的偏差是3，
你对自己预测的不确定 度是4度，他们平方相加再开方，就是5）。然后，你从温度计那里得到了
k时刻的温度值，假设是25度，同时该值的偏差是4度。
	由于我们用 于估算k时刻的实际温度有两个温度值，分别是23度和25度。究竟实际温度是多少呢？
相信自己还是相信温度计呢？究竟相信谁多一点，我们可以用他们的 covariance来判断。因为
Kg^2=5^2/(5^2+4^2)，所以Kg=0.78，我们可以估算出k时刻的实际温度值是：23+0.78* (25-23)=24.56度。
可以看出，因为温度计的covariance比较小（比较相信温度计），所以估算出的最优温度值偏向温度计的值。       
现 在我们已经得到k时刻的最优温度值了，下一步就是要进入k+1时刻，进行新的最优估算。到现在为止，
好像还没看到什么自回归的东西出现。对了，在进入 k+1时刻之前，我们还要算出k时刻那个最优值（24.56度）
的偏差。算法如下：((1-Kg)*5^2)^0.5=2.35。这里的5就是上面的k时 刻你预测的那个23度温度值的偏差，
得出的2.35就是进入k+1时刻以后k时刻估算出的最优温度值的偏差（对应于上面的3）。       
	就是这样，卡尔曼滤波器就不断的把covariance递归，从而估算出最优的温度值。他运行的很快，
而且它只保留了上一时刻的covariance。上面的Kg，就是卡尔曼增益（Kalman Gain）。他可以随不同的
时刻而改变他自己的值，是不是很神奇！
*/
float Q_angle=0.001, Q_gyro=0.003, R_angle=0.5, dt=0.005;   //注意：dt的取值为kalman滤波器采样时间;     
float P[2][2] = { { 1, 0 },     
                  { 0, 1 } };     
float Pdot[4] ={0,0,0,0}; 
const char C_0 = 1; 
float q_bias, angle_err, PCt_0, PCt_1, E, K_0, K_1, t_0, t_1;    
float angle;

void Kalman_Filter(float angle_m,float gyro_m)            //gyro_m:gyro_measure    
{     
	// X(k|k-1)=A X(k-1|k-1)+B U(k) .................................(1)
	// 我们的矩阵X为：
	//（ angle
    //   gyro ）
	//我们的矩阵A为：
	//（ 1     1
    //   0     1 ）
    angle += (gyro_m-q_bias) * dt;//先验估计   

	// P(k|k-1)=A P(k-1|k-1) A’+Q ...................................(2) 
	// Pdot是P的微分。    
	// 我们的Q是
	//（ Q_angle  0
    //   0   	  Q_gyro ）
    Pdot[0]=Q_angle - P[0][1] - P[1][0];// Pk-先验估计误差协方差的微分     
    Pdot[1]=- P[1][1];     
    Pdot[2]=- P[1][1];     
    Pdot[3]=Q_gyro;     
    P[0][0] += Pdot[0] * dt; // Pk- 先验估计误差协方差微分的积分    
    P[0][1] += Pdot[1] * dt; //  = 先验估计误差协方差     
    P[1][0] += Pdot[2] * dt;     
    P[1][1] += Pdot[3] * dt; 

    angle_err = angle_m - angle; //zk-先验估计

	// Kg(k)= P(k|k-1) H’ / (H P(k|k-1) H’ + R) ......................(4)
	// H是测量系统的矩阵，为（ 1
    //                          1 ） 
    PCt_0 = C_0 * P[0][0];     
    PCt_1 = C_0 * P[1][0];     
    E = R_angle + C_0 * PCt_0;     
    K_0 = PCt_0 / E;//Kk     
    K_1 = PCt_1 / E;   

	// P(k|k)=（I-Kg(k) H）P(k|k-1) ...................................(5)
    t_0 = PCt_0;     
    t_1 = C_0 * P[0][1]; 
    P[0][0] -= K_0 * t_0; //后验估计误差协方差    
    P[0][1] -= K_0 * t_1;     
    P[1][0] -= K_1 * t_0;     
    P[1][1] -= K_1 * t_1; 

	// X(k|k)= X(k|k-1)+Kg(k) (Z(k)-H X(k|k-1)) .......................(3)
    angle     += K_0 * angle_err; //后验估计     
    q_bias    += K_1 * angle_err; //后验估计     
    angle_dot  = gyro_m - q_bias; //输出值（后验估计）的微分 = 角速度     
}




//#include "stdio.h"
//#include "stdlib.h"
//#include "math.h"
// 
//double frand()
//{
//	return 2 * ((rand() / (double)RAND_MAX) - 0.5);//随机噪声
//}
// 
//void main()
//{
//	float x_last = 0;
//	float p_last = 0.02;
//	float Q = 0.018;
//	float R = 0.542;
//	float kg;
//	float x_mid;
//	float x_now;
//	float p_mid;
//	float p_now;
//	float z_real = 0.56;
//	float z_measure;
//	float summerror_kalman = 0;
//	float summerror_measure = 0;
//	int i;
//	x_last = z_real + frand()*0.03;
//	x_mid = x_last;
//	for (i = 0; i < 20;i++)
//	{
//		x_mid = x_last;
//		p_mid = p_last + Q;
//		kg = p_mid / (p_mid + R);
//		z_measure = z_real + frand()*0.03;//测量值
//		x_now = x_mid + kg*(z_measure - x_mid);//估计出的最有值
//		p_now = (1 - kg)*p_mid;//最优值对应的协方差
// 
//		printf("Real position:%6.3f\n", z_real);
//		printf("Measure position:%6.3f [diff:%.3f]\n", z_measure, fabs(z_real - z_measure));
//		printf("Kalman position: %6.3f [diff:%.3f]\n", x_now, fabs(z_real - x_now));
//		printf("\n\n");
//		summerror_kalman += fabs(z_real - x_now);
//		summerror_measure += fabs(z_real - z_measure);
//		p_last = p_now;
//		x_last = x_now;
//	}
//	printf("总体测量误差      :%f\n", summerror_measure);
//	printf("总体卡尔曼滤波误差:%f\n", summerror_kalman);
//	printf("卡尔曼误差所占比例:%d%%\n", 100 - (int)((summerror_kalman / summerror_measure) * 100));
// 
//	getchar();
//}