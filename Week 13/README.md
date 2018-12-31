# Preparation

# Lecture
## Seaborn - Ocean Temperature Profiles

1. [Plotting themes](https://python-graph-gallery.com/104-seaborn-themes/)
```
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('fivethirtyeight')
```

- [Style list](https://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html)

2. [Subplots](https://jakevdp.github.io/PythonDataScienceHandbook/04.08-multiple-subplots.html)
```
for i in range(1, 7):
    plt.subplot(2, 3, i)
    plt.text(0.5, 0.5, str((2, 3, i)),
             fontsize=18, ha='center')
```

3. [Controlling Aesthetics](https://seaborn.pydata.org/tutorial/aesthetics.html)
- [Overiding styles](https://seaborn.pydata.org/tutorial/aesthetics.html#overriding-elements-of-the-seaborn-styles)

## Algorithmic Learning Introduction

### Linear Regression

### Non-Linear Regression

### Advanced Techniques - Seasonal Trend Analysis Built on scikit-learn

# Classwork

# Homework

