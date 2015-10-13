from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

from example_tournaments import axelrod_strategies

strategy_names = list(map(str, axelrod_strategies()))
strategy_names = [x.replace('/', '-') for x in strategy_names]

heatmap_types_names = [("cooperation_heatmaps", "Cooperation Rate Heatmap"),
                       ("opponent_cooperation_heatmaps", "Opponent Cooperation Rate Heatmap"),
                       ("score_heatmaps", "Mean Score Heatmap"),
                       ("score_diff_heatmaps", "Mean Score Difference Heatmap")]

# Render individual strategy pages
for strategy_name in strategy_names:
    for (heatmap_directory, heatmap_name) in heatmap_types_names:
        template = env.get_template('strategy.template')
        md = template.render(heatmap_types_names=heatmap_types_names, strategy_name=strategy_name)
        filename = "strategies/{0}.md".format(strategy_name)
        with open(filename, 'w') as f:
            f.write(md)

# Render README.md
plottypes_headers = [("boxplot", "Score Distributions"),
                     ("winplot", "Win Distributions"),
                     ("payoff", "Pairwise Payoffs")]


tournament_info = [("AllFairStrategies", "All Fair Strategies", """This tournament covers all strategies in the Axelrod library that follow the standard Axelrod rules."""),
                         ("FiniteMemory", "Finite Memory", """The players in this tournament are all strategies that remember a finite number of rounds (i.e. do not retain history indefinitely)."""),
                         ("Memoryone", "Memory One", """The players in this tournament are all memoryone strategies (having memory depth 0 or 1)."""),
                         ("StewartPlotkin2012", "Stewart & Plotkin 2012", """This tournament covers the same strategies in [Stewart and Plotkin's 2012 tournament](http://www.pnas.org/content/109/26/10134.full.pdf)"""),
                         ( "tscizzle", "Tyler Singer-Clark","""This tournament's players are those used in Tyler Singer-Clark's paper [Morality Metrics On Iterated Prisoner's Dilemma Players](http://www.scottaaronson.com/morality.pdf)""")]

template = env.get_template('readme.template')
md = template.render(strategy_names=strategy_names,
                     tournament_info=tournament_info,
                     plottypes_headers=plottypes_headers)
filename = "README.md"
with open(filename, 'w') as f:
    f.write(md)