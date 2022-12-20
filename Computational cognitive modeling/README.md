**Instructors**: [Brenden Lake](https://cims.nyu.edu/~brenden/) and [Todd Gureckis](http://psych.nyu.edu/gureckis/)

**Teaching Assistants**: Yanli Zhou and Graham Flick

**Meeting time and location**:  
We have a "flipped classroom" model for lecture  
Lecture is pre-recorded and available on Vimeo  
Live discussion is on Mondays 1:35-2:35 PM  

Lab  
Tuesdays 2:40-3:30 PM  
Access via the Zoom link in NYU Classes

**Course numbers**:  
DS-GA 1016 (Data Science)  
PSYCH-GA 3405.002 (Psychology)  

**Contact information and Piazza**:  
We use Piazza for questions and class discussion. Piazza gets you help efficiently from classmates, the TA, and the instructors. Rather than emailing questions to the teaching staff, please post your questions on Piazza.

The signup link for our Piazza page is available here ([piazza.com/nyu/spring2020/dsga3001005](https://piazza.com/nyu/spring2020/dsga3001005)).

Once signed up, our class Piazza page is available here ([piazza.com/nyu/spring2020/dsga3001005/home](https://piazza.com/nyu/spring2020/dsga3001005/home)).

If you have a question that isn't suitable for Piazza and there is a need to email the teaching staff directly, please use the following email address: instructors-ccm-spring2020@nyuccl.org

**Office hours (via Zoom. Look for links posted on Piazza)**:  
Todd Gureckis (Tuesday at 1-2pm eastern)  
Brenden Lake (Tuesdays at 10-11am eastern)  
Yanli Zhou (Wednesdays at 1-2pm eastern)  
Graham Flick (Wednesdays at 3-4pm eastern)

**Summary**: This course surveys the leading computational frameworks for understanding human intelligence and cognition. Both psychologists and data scientists are working with increasingly large quantities of human behavioral data. Computational cognitive modeling aims to understand behavioral data and the mind and brain, more generally, by building computational models of the cognitive processes that produce the data. This course introduces the goals, philosophy, and technical concepts behind computational cognitive modeling.

The lectures cover artificial neural networks (deep learning), reinforcement learning, Bayesian modeling, model comparison and fitting, classification, probabilistic graphical models, and program induction. Modeling examples span a broad set of psychological abilities including learning, categorization, language, memory, decision making, and reasoning. The homework assignments include examining and implementing the models surveyed in class. Students will leave the course with a richer understanding of how computational modeling advances cognitive science, how cognitive science can inform research in machine learning and AI, and how to fit and evaluate cognitive models to understand behavioral data.

Please note that this syllabus is not final and there may be further adjustments.

## Pre-requisites
- Math: We will use concepts from linear algebra, calculus, and probability. If you had linear algebra and calculus as an undergrad, or if you have taken Math Tools in the psychology department, you will be in a good position for approaching the material. Familiarity with probability is also assumed. We will review some of the basic technical concepts in lab.

- Programming: Previous experience with Python is required. The assignments will use Python 3 and Jupyter Notebooks (http://jupyter.org). We will have a Python refresher in lab, and we also recommend this tutorial (http://openbookproject.net/thinkcs/python/english3e/).

## Grading
The final grade is based on the homeworks (60%) and the final project (40%). We also added this policy: We will drop the lowest grade (in percent correct) from the four homework assignments.

Class participation will be used to decide grades in borderline cases. As we only meet once a week, class attendance is obviously important for success in the class.

## Final Project
The final project proposal is due Monday, April 6 (0.5 pages written). Please submit via email to instructors-ccm-spring2020@nyuccl.org with the file name lastname1-lastname2-lastname3-ccm-proposal.pdf.

The final project is due Wednesday 5/13. Please submit via email to instructors-ccm-spring2020@nyuccl.org with the file name lastname1-lastname2-lastname3-ccm-final.pdf.

The final project will be done in groups of 3-4 students. A short paper will be turned in describing the project (approximately 6 pages). The project will represent either an substantial extension of one of the homeworks (e.g., exploring some new aspect of one of the assignments), implementing and extending an existing cognitive modeling paper, or a cognitive modeling project related to your research.  We provide a list of project ideas [here](final_project_ideas.md), but of course you do not have to choose from this list.

**The final project must relate to computational cognitive modeling and cannot be a purely machine learning / data science project.** Thus, your project must connect, in some way, to the human mind and behavior. This could be collecting (informally) behavioral data to compare your computational model to. Or you could compare your model against results in the litearture or particular dataset of human behavior or ratings. Or you could compare your algorithm with human intelligence in a more abstract sense. There are many ways to make the connection, but your final project must connect to computational cognitive modeling.

Write-ups should be organized and written as a scientific paper. It must include the following sections: Introduction (with review of related work), Methods/Models, Results, and Discussion/Conclusion. A good example would be to follow the structure of this paper from the class readings:
- Peterson, J., Abbott, J., & Griffiths, T. (2016). Adapting Deep Network Features to Capture Psychological Representations. Presented at the 38th Annual Conference of the Cognitive Science Society. [link here](http://cocosci.berkeley.edu/jpeterson/pdf/peterson-cogsci2016-adapting-deep.pdf)

Code submission is not required for the final project.

## Lecture schedule
Live discussion is on Mondays 1:35-2:35 PM (via NYU classes Zoom tool)        
- 1/27 : Introduction ([slides](lectures/lecture-01-introduction.pdf))
- 2/3 : Neural networks / Deep learning (part 1) ([slides](lectures/lecture-02-neural_nets.pdf))
  - Homework 1 assigned on 2/5 (Due 2/24) (instructions for accessing [here](retrieving_hw.md))
- 2/10 : Neural networks / Deep learning (part 2) ([slides](lectures/lecture-03-neural_nets.pdf))
- 2/17 : NO CLASS - President's day
- 2/24 : Reinforcement learning (part 1) ([slides](lectures/lecture-04-reinforcementlearning.pdf))
- 3/2 : Reinforcement learning (part 2) ([slides](lectures/lecture-05-reinforcementlearning.pdf))
  - Homework 2 assigned (Due 3/27) (instructions for accessing [here](retrieving_hw.md))
- 3/9 : Reinforcement learning (part 3) ([slides](lectures/lecture-06-reinforcementlearning.pdf))([video](https://vimeo.com/404085989))
- 3/16 : NO CLASS - Spring recess
- 3/23 : Bayesian modeling (part 1) ([slides](lectures/lecture-07-bayesian_modeling.pdf)) ([video](https://vimeo.com/399514147))
  - Homework 3 assigned (Due 4/13) (instructions for accessing [here](retrieving_hw.md))
- 3/30 : Bayesian modeling (part 2) (for slides see part 1) ([video](https://vimeo.com/400435600))
- 4/6 : Model comparison and fitting, tricks of the trade ([slides](lectures/lecture-09-modelfit.pdf))([video](https://vimeo.com/404348821))
  - Project proposal due (Monday April 6)
- 4/13 : Categorization ([slides](lectures/lecture-10-categorization.pdf)) ([video](https://vimeo.com/407047389))
  - Homework 4 assigned (Due 5/4) (instructions for accessing [here](retrieving_hw.md))
- 4/20 : Probabilistic Graphical models ([slides](lectures/lecture-11-graphical_models.pdf)) ([video](https://vimeo.com/407755101))
- 4/27 : Information sampling and active learning ([slides](lectures/lecture-12-activelearning.pdf)) ([video](https://vimeo.com/412183257))
- 5/4 : Program induction and language of thought models ([slides](lectures/lecture-13-program_induction.pdf)) ([video](https://vimeo.com/410406345))
- 5/11 : Computational Cognitive Neuroscience([slides](lectures/lecture-14-computational_cognitive_neuroscience.pdf))([video](https://vimeo.com/417071937))
- Conclusion video ([slides](lectures/conclusion.pdf))([video](https://vimeo.com/416908765)) 
- Final project due (Wednesday 5/13)

## Lab schedule
Tuesdays 2:40-3:30 PM (via NYU classes Zoom tool)  
- 1/28 : Python and Jupyter notebooks review
- 2/4 : Introduction to PyTorch
- 2/11 : No lab
- 2/18 : HW 1 Review
- 2/25 : No lab
- 3/3 : Reinforcement learning
- 3/10 : HW 2 Review
- 3/17 : SPRING RECESS
- 3/24 : Probability review
- 3/31 : No lab
- 4/7 : HW 3 Review
- 4/14 : No lab
- 4/21 : No lab
- 4/28 : HW 4 Review
- 5/5 : TBD
- 5/12 : No lab (classes end 5/11)

## Readings and slides
Papers are available for download on NYU Classes in the "Resources" folder.

**Neural networks and deep learning**
- McClelland, J. L., Rumelhart, D. E., & Hinton, G. E. The Appeal of Parallel Distributed Processing. Vol I, Ch 1.
- LeCun, Y., Bengio, Y. & Hinton, G. (2015). Deep learning. Nature 521:436–44.
- McClelland, J. L., & Rogers, T. T. (2003). The parallel distributed processing approach to semantic cognition. Nature Reviews Neuroscience, 4(4), 310-322.
- Elman, J. L. (1990). Finding structure in time. Cognitive Science, 14(2), 179-211.
- Peterson, J., Abbott, J., & Griffiths, T. (2016). Adapting Deep Network Features to Capture Psychological Representations. Presented at the 38th Annual Conference of the Cognitive Science Society.

**Reinforcement learning and decision making**
- Gureckis, T.M. and Love, B.C. (2015) Reinforcement learning: A computational perspective. Oxford Handbook of Computational and Mathematical Psychology, Edited by Busemeyer, J.R., Townsend, J., Zheng, W., and Eidels, A., Oxford University Press, New York, NY.
- Daw, N.S. (2013) "Advanced Reinforcement Learning" Chapter in Neuroeconomics: Decision making and the brain, 2nd edition
- Niv, Y. and Schoenbaum, G. (2008) “Dialogues on prediction errors” Trends in Cognitive Science, 12(7), 265-72.
- Nathaniel D. Daw, John P. O'Doherty, Peter Dayan, Ben Seymour & Raymond J. Dolan (2006). Cortical substrates for exploratory decisions in humans. Nature, 441, 876-879.

**Bayesian modeling**
- Russel, S. J., and Norvig, P. Artificial Intelligence: A Modern Approach. Chapter 13, Uncertainty.
- Tenenbaum, J. B., and Griffiths, T. L. (2001). Generalization, similarity, and Bayesian inference. Behavioral and Brain Sciences, 24(4), 629-640.
- Tenenbaum, J. B., Kemp, C., Griffiths, T. L., & Goodman, N. D. (2011). How to grow a mind: Statistics, structure, and abstraction. Science, 331(6022), 1279-1285.
- Ghahramani, Z. (2015). Probabilistic machine learning and artificial intelligence. Nature, 521(7553), 452.
- MacKay, D. (2003). Chapter 29: Monte Carlo Methods. In Information Theory, Inference, and Learning Algorithms.

**Rational versus mechanistic modeling approaches**
- Jones, M. & Love, B.C. (2011). Bayesian Fundamentalism or Enlightenment? On the Explanatory Status and Theoretical Contributions of Bayesian Models of Cognition. Behavioral and Brain Sciences (target article).
- Griffiths, T.L., Lieder, F., & Goodman, N.D. (2015). Rational use of cognitive resources: Levels of analysis between the computational and the algorithmic. Topics in Cognitive Science, 7(2), 217-229.

**Model comparison and fitting, tricks of trade**
- Wilson, R.C. and Collins, A.G.E. (2019). Ten simple rules for the computational modeling of behavioral data.  eLife 2019;8:e49547
- Pitt, M.A. and Myung, J (2002) When a good fit can be bad. Trends in Cognitive Science, 6, 10, 421-425.
- Roberts, S. & Pashler, H. (2000) How persuasive is a good fit? A comment on theory testing. Psychological Review, 107, 358-367.
- \[optional\] Myung, I.J. (2003). Tutorial on maximum likelihood estimation. Journal of Mathematical Psychology, 47, 90-100.

**Probabilistic graphical models**
- Charniak (1991). Bayesian networks without tears. AI Magazine, 50-63.
- Kemp, C., & Tenenbaum, J. B. (2008). The discovery of structural form. Proceedings of the National Academy of Sciences, 105(31), 10687-10692.
- \[optional\]  Russel, S. J., and Norvig, P. Artificial Intelligence: A Modern Approach. Chapter 14, Probabilistic reasoning systems.

**Program induction and language of thought models**
- Ghahramani, Z. (2015). Probabilistic machine learning and artificial intelligence. Nature, 521(7553), 452.
- Goodman, N. D., Tenenbaum, J. B., & Gerstenberg, T. (2014). Concepts in a probabilistic language of thought. Center for
Brains, Minds and Machines (CBMM).
- Lake, B. M., Salakhutdinov, R., & Tenenbaum, J. B. (2015). Human-level concept learning through probabilistic program induction. Science, 350(6266), 1332-1338.

**Computational Cognitive Neuroscience**
- Kreigeskorte, N. and Douglas, P.K. (2018) Cognitive computational neuroscience. Nature Neuroscience. 21(9): 1148-1160. doi:10.1038/s41593-018-0210-5
- Turner, B.M., Forstmann, B.U., Love, B.C., Palmeri, T.J., Van Maanen, L. (2017). Approaches to analysis in model-based cognitive neuroscience. Journal of Mathematical Psychology. 76(B), 65-79.


## Course policies and FAQ

**Auditing**:  
We can't accommodate more auditors at this point.

**Collaboration and honor code**:  
We take the collaboration policy and [academic integrity](https://cas.nyu.edu/content/nyu-as/cas/academic-integrity.html) very seriously. Violations of the policy will result in zero points and possible disciplinary referral. You may discuss the homework assignments with your classmates, but **you must run the simulations and complete the write-ups for the homeworks on your own.** Under no circumstance should students look at each other’s code or write ups, or code/write-ups from previous years of this course. Do not share your write up or code with any of your classmates under any circumstances.

**Dropping your lowest homework**:  
At the end of the semester, we will drop your lowest homework grade (in terms of % correct). We still encourage you to complete all of the homeworks, as we designed them to help solidify the course material and we hope they will be valuable to you. However this drop policy gives you flexibility if unexpected circumstances arise.

**Late work**:  
We will take off 10% for each day a homework or final project is late. Assignments should be turned in all-at-once and not in pieces. If an assignment is incomplete and later completed, the late penalty is applied to the entire assignment.

**Extensions**:  
If you are requesting an extension, email the teaching team (instructors-ccm-spring2020@nyuccl.org) and explain the reason. You must submit a request for extension at least 24 hours before the due date of the assignment.

**Regrading**:  
If you feel there was a mistake in the grading of your assignment, you can formally request a regrade by emailing the teaching team. This will prompt us to regrade the entire assignment and could lead to your grade being either raised or lowered depending on what the regrade finds. You can submit a regrade request via gradescope.

**Did you forget to turn in part of the homework, or did it print improperly?**:  
Before turning in your assignment, double check that all of your answers appear clearly in the PDF printout. We will not regrade a homework because your answer did not display correctly in the version you submitted.

**Extra credit**:  
No extra credit will be given, out of interest of fairness.

## Preconfigured cloud environment
Students registered for the course have the option of completing homework assignments on their personal computers, or in a cloud Jupyter environment with all required packages pre-installed. Students can log onto the environment using their nyu net ids [here](https://dsgs-3001005.rcnyu.org).
