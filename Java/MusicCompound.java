package test1;

import java.io.*;

public class MusicCompound 
{
    public static void compound()
    {
        FileOutputStream fileOutputStream = null;
        FileInputStream fileInputStream1 = null;
        FileInputStream fileInputStream2 = null;
        String fileNames[] = {"C:/Users/brucezhcw/Downloads/示例歌曲/何晟铭爱的供养.mp3","C:/Users/brucezhcw/Downloads/示例歌曲/杨幂爱的供养.mp3"};
        //设置byte数组，每次往输出流中传入8K的内容
        byte[] by = new byte[1024*200];//[1024*6];
        byte[] byby = new byte[1];
        try
        {
            fileOutputStream = new FileOutputStream("C:/Users/brucezhcw/Desktop/爱的供养.mp3");
            fileInputStream1 = new FileInputStream(fileNames[0]);
            fileInputStream2 = new FileInputStream(fileNames[1]);
            //fileInputStream1.skip(1024*1024*3);
            fileInputStream2.skip(1024*1036);
            for(int i=0;i<1024/200;i++)
            	if(fileInputStream1.read(by) != -1) 
            		fileOutputStream.write(by);
            for(int i=0;i<1024*6/200;i++)
            {
                if(i%2==0)
                {
                	if(fileInputStream1.read(by) != -1)                    
                		{
                			fileOutputStream.write(by);
                			fileInputStream2.read(by);
                		}
                }
                else
                {
                	if(fileInputStream2.read(by) != -1)                    
                		{
                			fileOutputStream.write(by);
                			fileInputStream1.read(by);
                		}
                }
                System.out.print(i + "  ");
            }
            while(fileInputStream1.read(byby) != -1)
            	fileOutputStream.write(byby);
        }
        catch(FileNotFoundException e)
        {
            e.printStackTrace();
        }
        catch(IOException e)
        {
            e.printStackTrace();
        }
        finally
        {
            try
            {
                //输出完成后关闭输入输出流
            	System.out.println("\nstart close()");
                fileInputStream1.close();
                fileInputStream2.close();
                fileOutputStream.close();
                System.out.println("close() over");
            } 
            catch(IOException e)
            {
                e.printStackTrace();
            }
        }
    }
}
