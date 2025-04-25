# 🎬 Movie Recommender System 🍿

A content-based movie recommendation system that suggests similar movies based on user preferences. Built using Python, Pandas, Scikit-learn, and Streamlit.

> **Looking for Bollywood movie recommendations?** Check out our Bollywood Movie Recommendation System: [https://github.com/fatima-amani/Bollywood-Movie-Recommendation-System](https://github.com/fatima-amani/Bollywood-Movie-Recommendation-System)


## ✨ Features

- 🔍 Recommends 6 most similar movies based on a selected title
- 📊 Uses movie metadata (genres, keywords, cast, crew, overview) for recommendations
- 🌐 Interactive Streamlit web interface for easy interaction
- 🖼️ Displays movie posters alongside recommendations using TMDB API

## 🛠️ Technologies Used

- **Python** 🐍 - Core programming language
- **Pandas** 🐼 - For data manipulation and preprocessing
- **Scikit-learn** 📊 - For TF-IDF vectorization and cosine similarity calculations
- **Streamlit** 📱 - For interactive web application development
- **TMDB API** 🎞️ - For fetching movie posters
- **TMDB dataset** 🎥 - For comprehensive movie data

## 📁 Files Structure

```
Movie-Recommender/
├── app.py                      # Streamlit application with UI
├── movie_recommender_model.ipynb  # Jupyter notebook with model development
├── movie_list.pkl              # Pickled movie data
├── similarity.pkl              # Pickled similarity matrix
├── tmdb_5000_credits.csv       # TMDB credits dataset
└── tmdb_5000_movies.csv        # TMDB movies dataset
```

## 🎞️ Dataset

The system uses the TMDB 5000 Movie Dataset which contains:
- 5000 movies with detailed metadata
- Credits information (cast and crew details)
- Features like budget, genres, keywords, overview, etc.

## ⚙️ How It Works

1. Data is preprocessed in the Jupyter notebook and important features are combined
2. Text data is vectorized using TF-IDF (Term Frequency-Inverse Document Frequency)
3. Cosine similarity between movies is calculated to find similarities
4. Results are exported as pickle files (`movie_list.pkl` and `similarity.pkl`)
5. Streamlit app imports these pickle files to make real-time recommendations
6. TMDB API is used to fetch movie posters for recommended movies

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/fatima-amani/Movie-Recommender.git
   cd Movie-Recommender
   ```

2. **Install required packages**:
   ```bash
   pip install streamlit pandas scikit-learn requests
   ```

3. **Generate model files**:
   - Run the `movie_recommender_model.ipynb` notebook to generate the pickle files
   - Ensure `movie_list.pkl` and `similarity.pkl` are created in the project root

4. **Run the Streamlit application**:
   ```bash
   streamlit run app.py
   ```

5. **Access the application** in your browser (typically at `http://localhost:8501`)

## 📱 Usage

1. Select a movie from the dropdown menu
2. Click "Get similar Recommendations" button
3. View the 6 recommended movies with their posters displayed in a grid layout


## 👩‍💻 Author

**Fatima Amani**  
GitHub: [@fatima-amani](https://github.com/fatima-amani)

