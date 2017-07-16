import numpy as np
from PIL import Image
#RGB
#000 Noire
#001 RED
#010 BLUE
#011 GREY
#100 GREEN
#101 YELLOW
#110 ORANGE
#111 WHITE
def scale_RGB(x):
    return x*1.0/255;
nb_inp=3;
nb_out=3;
nb_hidden=3;

def sigmoid(x,deriv=False):
    if (deriv==True):
        return (x)*(1-x);
    return 1/(1+np.exp(-x)); 
def trainRGB():
    X=np.array([[scale_RGB(250), scale_RGB(181),scale_RGB(127)],[1, scale_RGB(165), 0],  [1, scale_RGB(165), 0],#Orange
                             [scale_RGB(207), scale_RGB(75), scale_RGB(65)],[scale_RGB(173), scale_RGB(216), scale_RGB(230)], [0,0, scale_RGB(139)], #Blue
                             [scale_RGB(144), scale_RGB(238), scale_RGB(144)],[0,scale_RGB(100), 0], #Green
                             [scale_RGB(239),scale_RGB(239), scale_RGB(74)],[scale_RGB(242),scale_RGB(242), scale_RGB(62)],#Yellow
                             [scale_RGB(211),scale_RGB(211), scale_RGB(211)],[scale_RGB(169),scale_RGB(169), scale_RGB(169)],#Grey
                             [scale_RGB(4),scale_RGB(11), scale_RGB(19)],[scale_RGB(0),scale_RGB(0), scale_RGB(7)],[scale_RGB(8),scale_RGB(11), scale_RGB(28)],#Black
                             [scale_RGB(255),scale_RGB(255), scale_RGB(255)], [scale_RGB(254),scale_RGB(252), scale_RGB(250)] #White
                     ]);

    y=[[1,1,0],[1,1,0],
         [0,0,1],[0,0,1],
         [0,1,0],[0,1,0],
         [1,0,0], [1,0,0],
         [1,0,1], [1,0,1],
        [0,1,1], [0,1,1],
         [0,0,0],[0,0,0],[0,0,0],
         [1,1,1],[1,1,1]
           ]

    np.random.seed(1);
    syn0=2*np.random.random((nb_inp,nb_hidden))-1;
    syn1=2*np.random.random((nb_hidden,nb_out))-1;
    for i in xrange(10000):
        l0=X;
        l1=sigmoid(np.dot(l0,syn0));
        l2=sigmoid(np.dot(l1,syn1));
        l2_error=y-l2;
        l2_delta=l2_error*sigmoid(l2,deriv=True);
        l1_error=l2_error.dot(syn1.T);
        l1_delta=l1_error*sigmoid(l1,deriv=True);
        syn1 += np.dot(l1.T,l2_delta)
        syn0 += np.dot(l0.T,l1_delta)
    RGB_values=(8,103,167); 
    R,G,B=RGB_values
    Xtest=[scale_RGB(R),scale_RGB(G),scale_RGB(B)];
    l0=Xtest;
    l1=sigmoid(np.dot(l0,syn0));
    l2=sigmoid(np.dot(l1,syn1));
    return  (syn0,syn1);
def recognizeColor (url):
    syn0,syn1=trainRGB();
    img=Image.open(url);
    pix=img.load(); 
    width,height=img.size;
    black=0;
    purple=0;
    blue=0;
    red=0;
    orange=0;
    yellow=0;
    white=0;
    green=0;
    for y in range(0,height):
        for x in range(width):
            RGB_values=img.getpixel((x,y));
            R,G,B=RGB_values;
            Xtest=[scale_RGB(R),scale_RGB(G),scale_RGB(B)];
            l0=Xtest;
            l1=sigmoid(np.dot(l0,syn0));
            l2=sigmoid(np.dot(l1,syn1));
     
        
            if (round(l2[0],0)==0 and  round(l2[1],0)==0 and round(l2[2],0)==0 ):

                black=black+1;

            if (round(l2[0],0)==0 and round(l2[1],0)==0 and round(l2[2],0)==1 ):

                red=red+1;

            if (round(l2[0],0)==0 and round(l2[1],0)==1 and round(l2[2],0)==0 ):

                blue=blue+1;
     
            
            if (round(l2[0],0)==0 and  round(l2[1],0)==1 and round(l2[2],0)==1):
                purple=purple+1

            if (round(l2[0],0)==1 and round(l2[1],0)==0 and round(l2[2],0)==0 ):

                green=green+1


            if (round(l2[0],0)==1 and  round(l2[1],0)==0 and round(l2[2],0)==1 ):

                yellow=yellow+1

            if (round(l2[0],0)==1 and  round(l2[1],0)==1 and round(l2[2],0)==0 ):

                orange=orange+1
            

            if (round(l2[0],0)==1 and round(l2[1],0)==1 and round(l2[2],0)==1):
                white=white+1;
    tot =width*height;
    print 'Blue  :'+str((float(blue)/tot)*100); 
    print 'orange  :'+str((float(orange)/tot)*100);
    print 'purple  : '+str((float(purple)/tot)*100);
    print 'green : '+str((float(green)/tot)*100);
    print 'red : '+str((float(red)/tot)*100);
    print 'yellow: '+str((float(yellow)/tot)*100);
    print 'white: '+str((float(white)/tot)*100);
    print 'Black :'+str((float(black)/tot)*100);
    print '=================';
    print 100;

recognizeColor ("plant.jpeg");
