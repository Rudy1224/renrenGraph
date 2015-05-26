# renrenGraph
**Graphical demonstration of my relations on renren.com. Forks and pull requests are welcome.**<br>
This project is inspired by [@yueyoum](https://github.com/yueyoum) and his [**renren-relationship**](https://github.com/yueyoum/renren-relationship), but has simpler login process.<br>
Run `scraper.py` to download your relationship information on the local machine and use `local.py` to draw the graph.<br>
Graph is drawn with `networkx` and `matplotlib` therefore it's not that beautiful...   :(<br>
#####Sample Output Graph
Below is a graph showing the relationship of me and my renren friends. 2nd-degree friends who I don't know are removed to keep the graph tidy and easy to recognize.<br>
Clearly there are two clusters, containing my high school classmates and university ones respectively. I only have several primary and middle school classmates as friends on renren.com, so the groups are not so obvious.
![sample](https://raw.githubusercontent.com/Rudy1224/renrenGraph/master/figure_1.png)
