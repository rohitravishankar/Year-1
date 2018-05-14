##########################################
# CISC - 863 Statistical Machine Learning
# Rohit Ravishankar
# rr9105@rit.edu
##########################################


# Objective function
f <- function(x1, x2) {
  return (100 * ((x2-(x1^2))^2) + (1-x1)^2)
}

# Starting Parameters
x1 <- 6
x2 <- 6

#total number of iterations
iterations <- 1000

#learning rate
alpha <- 0.0001

#initial max value
maxValue <- 99999999999999999999999999999

#precision value at which we want to break the loop
precision <- 0.001

for(i in 1:iterations) {
  
  # Calculating x1 using the partial derivative of x1
  tempx1 <- x1 - alpha * (-400 * x1*(x2 - (x1^2)) - 2 * (1-x1))
  
  # Calculating x2 using the partial derivative of x2
  tempx2 <- x2 - alpha * 200 * (x2 - (x1^2))
  
  # When the iterations should stop
  if( abs(tempx1 - x1) < precision && abs(tempx2 - x2) < precision ) {
    break;
  }
  
  # Simultaneous update
  x1 <- tempx1
  x2 <- tempx2
}

#Results
print(paste0(" x1 = ", x1))
print(paste0(" x2 = ", x2))
print(paste0(" iterations = ", i))
print(paste0(" Value of function = ", f(x1,x2)))

# Answers
##########################################
# x1 = -2.48873368733961
# x2 = 6.20900503834059
# iterations = 14
# Value of function = 12.1943961529311
##########################################
