package Test;

public class Sort {
	
	//√∞≈›≈≈–Ú
	public static void bubbleSort(int[] array){
        boolean flag=true;
        for(int i=0;i<array.length-1 && flag;i++){
            flag=false;
            for(int j=0;j<array.length-1-i;j++){
                if(array[j]>array[j+1]){
                    int temp=array[i];
                    array[j]=array[j+1];
                    array[j+1]=temp;
                    flag=true;
                }
            }
        }
    } 
	//ºÚµ•—°‘Ò≈≈–Ú
	public static void selectionSort(int[] array){
        for(int i=0;i<array.length-1;i++){
            int mink=i;
            for(int j=i+1;j<array.length;j++){
                if(array[j]<array[mink]){
                    mink=j;
                }
            }
            if(mink!=i){
                int temp=array[mink];
                array[mink]=array[i];
                array[i]=temp;
            }
        }
    }
	//÷±Ω”≤Â»Î≈≈–Ú
	public static void insertSort(int[] array){
        int j;
        for(int i=1;i<array.length;i++){
            int temp=array[i];
            j=i-1;
            while(j>-1&&temp<array[j]){
                array[j+1]=array[j];
                j--;
            }
            array[j+1]=temp;
        }
    } 
	//œ£∂˚≈≈–Ú
	public static void xier(int[] a,int n){
        for(int gap=n/2;gap>0;gap=gap/2){
            for(int i=gap;i<n;i++){
                int temp=a[i];
                int j=i-gap;
                while(j>=0 && temp<a[j]){
                    a[j+gap]=a[j];
                    j=j-gap;
                }
                a[j+gap]=temp;
            }
        }
    }
	//øÏÀŸ≈≈–Ú
	public static void quickSort(int[] s,int left,int right){
        if(left<right){
            int i=left,j=right,temp=s[left];
            while(i<j){
                while(i<j && s[j]>=temp){
                    j--;
                }
                if(i<j){
                    s[i++]=s[j];
                }
                while(i<j && s[i]<temp){
                    i++;
                }
                if(i<j){
                    s[j--]=s[i];
                }
            }
            s[i]=temp;
            quickSort(s,left,i-1);
            quickSort(s,i+1,right);
        }
    }
	//∂—≈≈–Ú
	public static void heapSortAsc(int[] a, int n) {
		int i,tmp;
		for (i = n / 2 - 1; i >= 0; i--)
			maxHeapDown(a, i, n-1);
		for (i = n - 1; i > 0; i--) {
			tmp = a[0];
			a[0] = a[i];
			a[i] = tmp;
			maxHeapDown(a, 0, i-1);
		}
	}
	private static void maxHeapDown(int[] a, int start, int end) {
		 int c = start;
		 int l = 2*c + 1;
		 int tmp = a[c];
		 for (; l <= end; c=l,l=2*l+1) {
			 if ( l < end && a[l] < a[l+1])
				 l++;
			 if (tmp >= a[l])
				 break;
			 else {
				 	a[c] = a[l];
				 	a[l]= tmp;
			 }
		 }
	}
	//πÈ≤¢≈≈–Ú
	public static void mergeSort(int[] nums, int low, int high){    	    	
		if(low<high){
			int mid = (low+high)/2;
			mergeSort(nums, low, mid);    		   		
			mergeSort(nums, mid+1, high);    		   		
			merge(nums, low, mid, high);    	
			}    	   
	}    
	private static void merge(int[] nums, int low, int mid, int high) {	 	
		int[] temp = new int[high-low+1];    	
		int i = low;    	
		int j = mid+1;    	
		int k = 0;    	
		while(i<=mid && j<=high){    		
			if(nums[i]<nums[j])    			
				temp[k++] = nums[i++];    		
			else    			
				temp[k++] = nums[j++];    	
		}    	 	
		while(i<=mid){    		
			temp[k++] = nums[i++];    	
		}    	
		while(j<=high){    		
			temp[k++] = nums[j++];    	
		}    	  	
		for (int k2 = 0; k2 < temp.length; k2++) {			
			nums[k2+low] = temp[k2];		
		}	
	}
	//Õ∞≈≈–Ú
	public static void bucketSort(int[] a, int max) {
	    int[] buckets;
		if (a==null || max<1)
			return ;
		buckets = new int[max];
		for(int i = 0; i < a.length; i++) 
			buckets[a[i]]++; 
		for (int i = 0, j = 0; i < max; i++) {
			while( (buckets[i]--) >0 ) {
				a[j++] = i;
			}
		}
		buckets = null;
	}
	//ª˘ ˝≈≈–Ú1
	public static void radixSort2(int[] number)
    {
		int d = getexp(getMax(number));
		int k = 0;
        int n = 1;
        int[][]temp = new int[10][number.length];
        int[]order = new int[10];
        while(d-->0)
        {
            for(int i = 0; i < number.length; i++)
            {
                int lsd = ((number[i] / n) % 10);
                temp[lsd][order[lsd]] = number[i];
                order[lsd]++;
            }
            for(int i = 0; i < 10; i++)
            {
                if(order[i] != 0)
                    for(int j = 0; j < order[i]; j++)
                    {
                        number[k] = temp[i][j];
                        k++;
                    }
                order[i] = 0;
            }
            n *= 10;
            k = 0;
        }
    }
	//ª˘ ˝≈≈–Ú2
	public static void radixSort(int[] a) {
		 int exp;
		 int max = getMax(a);
		 for (exp = 1; max/exp > 0; exp *= 10)
			 countSort(a, exp);
	}
	private static int getexp(int a) {
		 int exp = 0;
		 while(a>0) {
			 exp++;
			 a /= 10;
		 }
		 return exp;
	}
	private static int getMax(int[] a) {
		 int max;
		 max = a[0];
		 for (int i = 1; i < a.length; i++)
		 if (a[i] > max)
		 max = a[i];
		 return max;
	}
	private static void countSort(int[] a, int exp) {
		 int[] output = new int[a.length];
		 int[] buckets = new int[10];
		 for (int i = 0; i < a.length; i++)
			 buckets[ (a[i]/exp)%10 ]++;
		 for (int i = 1; i < 10; i++)
			 buckets[i] += buckets[i - 1];
		 for (int i = a.length - 1; i >= 0; i--) {
			 output[buckets[ (a[i]/exp)%10 ] - 1] = a[i];
			 buckets[ (a[i]/exp)%10 ]--;
		 }
		 for (int i = 0; i < a.length; i++)
			 a[i] = output[i];
		 output = null;
		 buckets = null;
	}
    //÷˜∫Ø ˝
	public static void main(String[] args) {
		int[] a= {19,16,18,7,9,8,10,4,3,6,15,13,12,11,14,2,17,1,20,5};
		System.out.println("before:");
		for(int i=0;i<20;i++){
			System.out.print(a[i]);
			System.out.print(" ");
		}
		mergeSort(a,0,19);
		System.out.println("\n\nafter:");
		for(int i=0;i<20;i++){
			System.out.print(a[i]);
			System.out.print(" ");
		}
	}

}