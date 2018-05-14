##########################################
# CISC - 863 Statistical Machine Learning
# Quiz 2
# Rohit Ravishankar
# rr9105@rit.edu
##########################################

# Graphing packages
library(ggplot2)
library(dplyr)

# Data from mycourses put into a list
D <- c(3.2877564, 3.3049376, 3.0065537, 2.4179332, 2.4255153, 3.3632328,
       3.3750101, 3.6351869, 2.5573695, 2.4708438, 2.7914828, 2.8363451,
       3.5001336, 2.7917707, 2.3019892,2.8733925, 2.4083626, 2.9122397,
       3.1874000, 3.3319748)

# Mean of the data
mu <- mean(D)

# Creating data to show a normal distribution
X <- seq( -35 , 35 , length=1000)
Prior <- dnorm(X, 0, 6)
Likelihood <- dnorm(X, mu, 10)
posteriorMean <- calculatePosteriorMean(0, 36, 100, D, length(D))
posteriorVariance <- calculatePosteriorVariance(36, length(D), 100)
Posterior <- dnorm(X, posteriorMean, posteriorVariance )
data <- data.frame(X, Prior, Likelihood, Posterior)

# Plotting prior, likelihood and posterior
ggplot(data, aes(X)) + 
  geom_line(aes(y = Prior, color = "blue")) +
  geom_line(aes(y = Likelihood, color = "red"))+
  geom_line(aes(y = Posterior, color = "green"))+
  theme_minimal()+
  scale_color_discrete(name = "Probability", labels = c("Prior","Posterior", "Likelihood"))+
  ylab("Probability Density")+
  xlab("X")

# Calculating the mean of the posterior function
calculatePosteriorMean <- function(mu0, variance0, variance, D, N) {
  a1 <- (1/variance0) + (N/variance)
  a1 <- 1/a1
  a2 <- mu0/variance0 + sum(D)/variance
  return(a1*a2)
}

# Calculating the variance of the posterior function
calculatePosteriorVariance <- function(variance0, N, variance) {
  y <- (1/variance0) + (N/variance)
  y <- y^-1
  return(y)
}