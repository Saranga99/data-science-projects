Introduction
  Linear Regression is a supervised machine learning algorithm where the predicted output is continuous and has a constant slope. It’s used to predict values within a continuous range, (e.g. sales, price) rather than trying to classify them into categories (e.g. cat, dog). There are two main types:


Simple regression
  Simple linear regression uses traditional slope-intercept form, where m and b are the variables our algorithm will try to “learn” to produce the most accurate predictions. x represents our input data and y represents our prediction.

            y=mx+b
Multivariable regression
  A more complex, multi-variable linear equation might look like this, where w represents the coefficients, or weights, our model will try to learn.

            f(x,y,z)=w1x+w2y+w3z

The variables x,y,z represent the attributes, or distinct pieces of information, we have about each observation. For sales predictions, these attributes might include a company’s advertising spend on radio, TV, and newspapers.

            Sales=w1Radio+w2TV+w3News
