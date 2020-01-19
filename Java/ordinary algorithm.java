package test1;

public class test1 {
	
	//斐波那契数列
	public static long funFib2(long index) {     
		long f0 = 0;    
		long f1 = 1;    
		long f2 = 1;     
		if (index == 0) {        
			return f0;    
		} 
		else if (index == 1) {        
			return f1;    
		} else if (index == 2) {        
			return f2;    
		}     
		for (int i = 3; i <= index; i++) {        
			f0 = f1;        
			f1 = f2;        
			f2 = f0 + f1;    
		}     
		return f2;
	}
}
