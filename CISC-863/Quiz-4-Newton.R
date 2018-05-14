##########################################
# CISC - 863 Statistical Machine Learning
# Rohit Ravishankar
# rr9105@rit.edu
##########################################


# Objective function
f <- function(x1, x2) {
  return (100 * ((x2-(x1^2))^2) + (1-x1)^2)
}

# Hessian Matrix H
# [ 1200 * (x1^2) - 400 * x2 + 2        -400 * x1         ]
# [ -400 * x2                             200             ]

# H^-1
# [    200                              400 * x1                                ]
# [ 400 * x2                           1200 * (x1^2) - 400 * x2 + 2             ]

# ad - bc term of inverse
const <- 240000 * (x1^2) - 160000 * x1 * x2 - 80000 * x2 + 400

# G - first order partial derivative of function f
# [  -400 * x1 * (x2 -  (x1^2)) - 2(1-x1)  ]
# [   200(x2-(x1^2))                       ]


# Starting Parameters
x1 <- 2
x2 <- 2

#total number of iterations
iterations <- 1000

#precision value at which we want to break the loop
precision <- 0.1

for(i in 1:iterations) {
  # (H^-1) * G
  new_X1 = 200 * (-400 * x1 *(x2 - (x1^2)) - 2 * (1-x1)) + 400 * x1 * (200 * (x2 - (x1^2)))
  new_X2 = 400 * x2 * ( -400 * x1 * (x2 - (x1^2)) - 2 * (1-x1) ) + 200* (x2 - (x1^2)) * (1200 * (x1^2) - (400 * x2) + 2)

  # To account for the constant term in the inverse
  new_X1 = new_X1/const
  new_X2 = new_X2/const

  tempX1 = x1 - new_X1
  tempX2 = x2 - new_X2
  
  # When the iterations should stop
  if( abs(tempX1 - x1) < precision && abs(tempX2 - x2) < precision ) {
    break;
  }
  
  # Simultaneous update
  x1 <- tempX1
  x2 <- tempX2
}

#Results
print(paste0("x1 = ",x1))
print(paste0("x2 = ",x2))
print(paste0(" iterations = ", i))
print(paste0(" Value of function = ", f(x1,x2)))

# Answers
##########################################
# x1 = 1.99750623441397
# x2 = 3.99002493765586
# iterations = 2
# Value of function = 0.995018691562159
##########################################


