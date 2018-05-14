##########################################
# CISC - 863 Statistical Machine Learning
# Rohit Ravishankar
# rr9105@rit.edu
##########################################
require(boot)

trainData <- read.table("/Users/rohitravishankar/Desktop/Statistical Machine Learning/traindata.txt")
testData <- read.table("/Users/rohitravishankar/Desktop/Statistical Machine Learning/testinputs.txt")
degree = 1:12
MSE <- c()
prediction <- c()
for(i in degree) {
  fit <- glm(V9 ~ poly(V1,i)+poly(V2,i)+poly(V3,i)
             +poly(V4,i)+poly(V5,i)+poly(V6,i)+poly(V7,i)
             +poly(V8,i), data = trainData)
  prediction[[i]] <- predict(fit, newdata = testData)
  MSE[i] <- cv.glm(trainData, fit, K = 8)$delta[1]
}
optimalK <- which.min(MSE)
write.table(as.data.frame(prediction[optimalK]), file = "testOutput.txt")

