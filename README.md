# Bayesian
<h3>Bayesain change-point detection model</h3>
Bayesain change-point detection model  is created to detect change points, it  uses
reparameterization techniques to select the prior distribution for the parameters of 
datadistribution.Then,the posterior distribution of the change point time and hyperparameters
are obtained by MCMC sampling, the location of the change point is get by the posterior probability.
<br>
<strong>Citation:</strong> ????

<h3>Requires</h3>
<ul>
<li>pymc3</li>
<li>pandas</li>
</ul>
<h3>Install</h3>
git clone git@https://github.com/sunnyxyf/Bayesian.git
<h3>A Short Intrduction of Our Work</h3>
Alternative Transcription Start Site (ATSS) is a major driving force for increasing the complexity
of transcripts in human tissues.We created a Bayersian change-point model for the relative ATSS usage as a 
percentage data, which could accurately predict change point locations. With comprehensive simulation studies, 
the performance of this model is consistently powerful and robust across most secnarios with different sample
sizes and Beta distributions. Besides, we also applied this method to a real ATSS longitudinal dataset and performed
pathway analysis and TF motif and enrichment analysis to demonstrate its effectiveness of our novel framework and
provide biological insights from the results.

<h3>Contact</h3>
If you have any questions or suggestions, please mail to 2414271896@qq.com or niuxiaoh@mail.hzau.edu.cn.
