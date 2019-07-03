## The Perceptron Algorithm 1.1
## xMIT - 6.86x
## Lecture 2. Linear Classifier and Perceptron - The Perceptron Algorithm
## Guilherme Kinzel - Student


## Features
Data = data.frame()
Data = rbind(Data, c(1,1))
Data = rbind(Data, c(1/3,-1))
Data = rbind(Data, c(-1,-3))
Data = rbind(Data, c(-2,-1))
Data = rbind(Data, c(-2/3,1))
Data = rbind(Data, c(-2/3,2))

## Labels
Y1 = c(1,1,1,-1,-1,-1)

## 
FuncaoXX = function(theta,theta_0,x)
{
  Num = -(theta[1]*x)-theta_0
  Den = theta[2]
  return(Num/Den)
}

Points = c(-10,10) ##plot propuses
ChangesThetaIDid = 0

theta = as.vector(rep(0,length.out=dim(Data)[2]))
theta_0 = 0
thetas = data.frame()

for(t in 1:30)
{
  for(i in 1:dim(Data)[1])
  {
    if(as.numeric(Y1[i]*(t(as.matrix(theta)) %*% 
                         as.numeric(Data[i,]))+theta_0)<=0)
    {
      theta = theta + Y1[i]*as.numeric(Data[i,])
      theta_0 = theta_0 + Y1[i]
      
      ## Plot features
      ChangesThetaIDid = ChangesThetaIDid + 1
      plot(Data, pch=ifelse(Y1==1,15,21), main=paste0("WhereIAm ", ChangesThetaIDid, 
                                                      "\nTheta: (",theta[1],",",theta[2],") Theta_0: ",theta_0),
           xlab="X1", ylab="X2",lwd=2, col=ifelse(Y1==1,"green","red"), 
           bg=ifelse(Y1==1,"green","red"))
      abline(h=0)
      abline(v=0)
      lines(x = Points, y = FuncaoXX(theta,theta_0,Points),col='blue',lty=2,lwd=2)
      
      thetas = rbind(thetas, theta)
    }
  }
}

print(thetas)