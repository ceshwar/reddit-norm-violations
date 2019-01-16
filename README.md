# reddit-norm-violations
* Working with over 2.8M removed comments collected from 100 different communities on Reddit, we identified 8 macro norms, i.e., norms that are widely enforced on most parts of Reddit. We extracted these macro norms by employing a hybrid approach---classification, topic modeling, and open-coding—--on comments identified to be norm violations within at least 85 out of the 100 study subreddits. Finally, we labelled over 40K Reddit comments removed by moderators according to the specific type of macro norm being violated, and make this dataset publicly available.

* For each of the labeled topics, we identified the top 5000 removed comments that were best fit by the LDA topic model. In this way, we identified over 5000 removed comments that are examples of each type of macro norm violation described in the paper. The removed comments were sorted by their topic fit, stored into respective files based on the type of norm violation they represent, and are made available on this repo.

* Results of open-coding are available here (mapping topic to macro norm)- https://docs.google.com/spreadsheets/d/1H7b28iRrKJiHGDqlmQ2Lc8S7bqwFjq8Jc-IgHUIm5Ig/edit?usp=sharing

