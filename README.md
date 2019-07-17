# Hybrid Approaches to Detect Comments Violating Macro Norms on Reddit: reddit-norm-violations

Authors: Eshwar Chandrasekharan (eshwar3@gatech.edu), Eric Gilbert (eegg@umich.edu)

This dataset was generated as an extension of our CSCW paper: 

*Eshwar Chandrasekharan, Mattia Samory, Shagun Jhaver, Hunter Charvat, Amy Bruckman, Cliff Lampe, Jacob Eisenstein, and Eric Gilbert. 2018. The Internet’s Hidden Rules: An Empirical Study of Reddit Norm Violations at Micro, Meso, and Macro Scales. Proceedings of the ACM on Human-Computer Interaction 2, CSCW (2018), 32.*

More details about the dataset can be found on arXiv: https://arxiv.org/abs/1904.03596

DOI: https://doi.org/10.5281/zenodo.3338698

Working with over 2M removed comments collected from 100 different communities on Reddit (subreddit names listed in data/study-subreddits.csv), we identified 8 macro norms, i.e., norms that are widely enforced on most parts of Reddit. We extracted these macro norms by employing a hybrid approach—classification, topic modeling, and open-coding—on comments identified to be norm violations within at least 85 out of the 100 study subreddits. Finally, we labelled over 40K Reddit comments removed by moderators according to the specific type of macro norm being violated, and make this dataset publicly available.

For each of the labeled topics, we identified the top 5000 removed comments that were best fit by the LDA topic model. In this way, we identified over 5000 removed comments that are examples of each type of macro norm violation described in the paper. The removed comments were sorted by their topic fit, stored into respective files based on the type of norm violation they represent, and are made available on this repo.

Here we make the following datasets publicly available:

* 1 file containing the log of all removed comments obtained from the top 100 subreddits between May 2016 to March 2017, after filtering out the following comments: 1) comments by u/AutoModerator, 2) replies to removed comments (i.e., children of the poisoned tree - refer to the paper for more information), and 3) non-readable comments (not utf-8 encoded).

* 8 files, each containing 5000+ removed comments obtained from Reddit, are stored in: data/macro-norm-violations/ , and they are split into different files based on the macro norm they violated. Each new line in the files represent a comment that was posted on Reddit between May 2016 to March 2017, and subsequently removed by subreddit moderators for violating community norms. All comments were preprocessed using the script in code/preprocessing-reddit-comments.py , in order to do the following: 1. remove new lines, 2. convert text to lowercase, and 3. strip numbers and punctuations from comments.

**Descriptions of each file containing 5059 comments(that were removed from Reddit, and preprocessed) violating macro norms present in data/macro-norm-violations/**: 
* "macro-norm-violations-n10-t0-misogynistic-slurs.csv" - Comments that use misogynistic slurs.
* "macro-norm-violations-n15-t2-hatespeech-racist-homophobic.csv" - Comments containing hate speech that is racist or homophobic.
* "macro-norm-violations-n10-t3-opposing-political-views-trump.csv", "macro-norm-violations-n15-t10-opposing-political-views-trump.csv" -  Comments with opposing political views around Trump (depends on originating sub).
* "macro-norm-violations-n10-t4-verbal-attacks-on-Reddit.csv" - Comments containing verbal attacks on Reddit or specific subreddits.
* "macro-norm-violations-n10-t5-porno-links.csv" - Comments with pornographic links.
* "macro-norm-violations-n10-t8-personal-attacks.csv", "macro-norm-violations-n10-t9-personal-attacks.csv"- Comments containing personal attacks.
* "macro-norm-violations-n15-t3-abusing-and-criticisizing-mods.csv" - Comments abusing and criticisizng moderators.
* "macro-norm-violations-n15-t9-namecalling-claiming-other-too-sensitive.csv" - Comments with name-calling, or claiming that the other person is too sensitive.

**Description of 1 file containing over 2M removed comments from 100 subreddits present in data/**

"reddit-removal-log.csv" - all comments that were removed from the 100 study subreddits during the study period described above (post-filtering).

Results of open-coding are available here (mapping topic to macro norm)- https://docs.google.com/spreadsheets/d/1H7b28iRrKJiHGDqlmQ2Lc8S7bqwFjq8Jc-IgHUIm5Ig/edit?usp=sharing
