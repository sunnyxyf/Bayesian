# Bayesian
<h3>Bayesain change-point detection model</h3>
<p>
Bayesain change-point detection model in this paper is created to detect change point for the relative
ATSS usage as a percentage data, Beta distribution is applied to fit the longitudinal ATSS data in this 
Bayesian model.Then, we use reparameterization techniques to select the prior distribution for the 
parameters of Beta distribution and the prior distribution of change point is determined to be discrete
uniform distribution. Finally,the posterior distribution of the change point and hyperparameters are 
obtained by MCMC sampling.
</p>
<p>
<strong>Citation:</strong> Juan Xia<sup>#</sup>, Haotian Zhu , Feiyang Xue , Nana Li*  and Feng Shi*(2022), An Bayesian 
  change-point model for  Alternative Transcription Start Site (ATSS) longitudinal data by next-generation RNA sequencing
</p>
<h3>Requires</h3>
<ul>
<li>pymc3</li>
<li>pandas</li>
</ul>
<h3>Install</h3>
git clone git@https://github.com/sunnyxyf/Bayesian.git
<h3>A Short Intrduction of Our Work</h3>
<p>Alternative Transcription Start Site (ATSS) is a major driving force for increasing the complexity
of transcripts in human tissues. The change-point detection algorithms are the effective methods to 
investigate the longitudinal dataset like the relative ATSS usage as a percentage data, which could 
identify the time point dividing a time series into tow segments where each segment has its own statstical
characteristics.</p>
<p>In this paper,first, one change-point detection model is constructed for each differential ATSS event,
the change points for these differential ATSS events are determined from the posterior distributions of
τ (at a certain time point τ, which happened an abrupt variation in time series data and may represent
transitions between different states). Using the detection of one change-point model,it is found that
the posterior probabilities of multiple time points are close for a few differential ATSS events. For
these differential ATSS events, this study constructed two change-point detection model, the change points 
for these differential ATSS events are determined from the posterior distributions of τ<SUB>1</SUB> and τ<SUB>2</SUB> (in time series
  , there exists two change points, τ<SUB>1</SUB> and τ<SUB>2</SUB>, where τ<SUB>1</SUB> < τ<SUB>2</SUB> ). Based on the one and two change-points Bayesian
detection models, the differential ATSS events are clustered according to the time of the change point.</p> 
<p>Next,we focused on evaluating the impact of sample sizes and difference in Beta distribution, with comprehensive
simulation studies, the performance of this model is consistently powerful and robust across most secnarios with
different sample sizes and Beta distributions.</p>
<p>Finally, according to the results of clustering, we applied this model to the real ATSS longitudinal dataset and 
performed pathway analysis and TF motif and enrichment analysis to demonstrate its effectiveness of our novel 
framework and provide biological insights from the results.</p>

<h3>Contact</h3>
If you have any questions or suggestions, please mail to 2414271896@qq.com or shifeng@mail.hzau.edu.cn.
