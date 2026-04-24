import pickle


user_movie=pickle.load(open("models/user_movie.pkl", "rb"))
similarity_df=pickle.load(open("models/similarity.pkl", "rb"))

def recommend(user_id):

    similar_users=similarity_df[user_id].sort_values(ascending=False)[1:6]
    similar_movies=user_movie.loc[similar_users.index]
    recommended=similar_movies.mean().sort_values(ascending=False) 
    watched=user_movie.loc[user_id]
    recommended=recommended[watched ==0]
    return list(recommended.head(5).index)