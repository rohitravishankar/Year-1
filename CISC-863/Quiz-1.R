##########################################
# CISC - 863 Statistical Machine Learning
# Rohit Ravishankar
# rr9105@rit.edu
##########################################

# Graphing packages
library(ggplot2)
library(dplyr)

i = 1 # To account for iterations
Nh = 4  # Number of heads observed
Nt = 1  # Number of tails observed

# Data Frame to store the results of the prior, likelihood and posterior
df_list = list()

# Fh and Ft represent the fictitious head and fictitious tail value
for(Fh in c(0.5, 2)){
  for(Ft in c(0.5, 2)){
    theta = seq(0, 1, 0.01)
    
    # Calculating the prior, likelihood and posterior values
    prior = dbeta(theta, shape1=Fh, shape2=Ft)
    likelihood = ((theta^Nh) * ((1-theta)^Nt))
    posterior = dbeta(theta, shape1 = Nh+Fh, shape2=Nt+Ft)
    
    # Preparing data frame
    df_list[[i]] = data.frame(theta=theta, prior=prior, likelihood=likelihood, posterior = posterior, group = paste("Nh =", Nh, "Nt =", Nt, "Fh =", Fh, "Ft =", Ft))
    i = i + 1
  }
}



df = bind_rows(df_list)
ggplot(df, aes(theta)) + 
  geom_line(aes(y = prior, color = "red")) +
  geom_line(aes(y = likelihood, color = "blue")) +
  geom_line(aes(y = posterior, color = "green")) +
  facet_wrap(~ group)+
  scale_color_discrete(name = "Probability", labels = c("Likelihood", "Posterior", "Prior"))+
  theme_minimal()+
  ylab("")+
  xlab("Theta")