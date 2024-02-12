import numpy as np
import string

def tokenize_text(s):
    """
    Tokenize the given sentences into a list of words
    Input:  s = the input sentence
    Output: word tokens
    """
    s_lower = s.lower()
    for char in string.whitespace + string.punctuation:
        s_lower = s_lower.replace(char, " ")
    tokens = s_lower.split()
    return tokens

def read_textfile(f):
    """
    Read text file split by new lines
    """
    with open(f, 'r') as f:
        return [s.strip() for s in f.readlines()]

def compute_bow(tokens, vocab):
    """
    Compute Bag-of-Words representation of the sentence given as word tokens according to the vocabulary
    Input:  tokens = a list of word tokens in the sentence
            vocab = a list of keywords for creating BoW.
    Output: 1D numpy array BoW representation of the sentence
    """
    return np.array([tokens.count(w) for w in vocab])

def compute_tf(sentence_bow):
    """
    Compute TF of the sentence using log10(count(t,d) + 1) 
    Input:  sentence_bow = a 1D numpy array BoW representation of the sentence
    Output: a 1D numpy array TF of the sentence
    """
    return np.array([np.log10(tf+1) for tf in sentence_bow])

def compute_idf(bow):
    """
    Compute IDF of the corpus using log10(N / dft) 
    Input:  bow = 2D numpy array BoW representation of all sentences in the corpus
    Output: a 1D numpy array IDF of all vocabulary
    """    
    val = np.zeros(bow.shape[1])
    for i in range(bow.shape[1]):
        for j in range(bow.shape[0]):
            if bow[j][i] > 0:
                val[i] += 1
    return np.array([np.log10(bow.shape[0]/(float(dft))) for dft in val])

def cosine_similarity(v1, v2, eps=1e-16):
    """
    Compute the cosine similarity between two vectors
    Input:  v1 = vector 1
            v2 = vector 2
            eps = a constant to avoid zero division
    Output: the cosine similarity between vector 1 and vector 2
    """
    return np.dot(v1, v2) / (np.dot(v1,v1)**.5 * np.dot(v2,v2)**.5 + eps)

def get_top_5(bow, query):
    """
    Find 5 sentences with the highest cosine similarity to the query sentence
    Input:  bow = 2D numpy array BoW representation of all sentences in the corpus
            query = a 1D array BoW representation of the query sentence
    Output: index of the 5 sentences in the corpus with the highest cosine similarity
    """
    num_sentences = bow.shape[0]
    score = np.zeros((num_sentences))
    for i in range(num_sentences):
        score[i] = cosine_similarity(query, bow[i])
    return score.argsort()[-5::]


if __name__ == "__main__":
    text_file = 'imdb_data.txt'
    vocab_file = 'vocab.txt'
    try:
        sentences = read_textfile(text_file)
        data = [tokenize_text(line) for line in sentences]
        vocab = read_textfile(vocab_file)
        print('Vocabulary = ', vocab)

        # create bag-of-word representation
        num_vocabs = len(vocab)
        num_sentences = len(sentences)
        
        bow = np.zeros((num_sentences, num_vocabs))
        tf = np.zeros((num_sentences, num_vocabs))
        for i in range(num_sentences):
            bow[i] = compute_bow(data[i], vocab)
            tf[i] = compute_tf(bow[i])
        
        # Compute IDF
        idf = compute_idf(bow)
        # compute TFIDF
        tfidf = tf * idf

        # test cosine similarity
        sample_sent1 = 'Tenet is such a great great movie that I would recommend everyone to watch this movie.'
        token1 = tokenize_text(sample_sent1)
        spl_bow1 = compute_bow(token1, vocab)
        tfidf1 = compute_tf(spl_bow1) * idf

        # similar sentence
        sample_sent2 = 'I recommend Mulan if you are looking for a good movie.'
        token2 = tokenize_text(sample_sent2)
        spl_bow2 = compute_bow(token2, vocab)
        tfidf2 = compute_tf(spl_bow2) * idf

        print('TFIDF')
        print('\t Sample sentence 1: ', sample_sent1)
        print('\t Sample sentence 2: ', sample_sent2)
        print(f'\t\t cosine similarity between sentence 1 and sentence 2 = {cosine_similarity(tfidf1, tfidf2):.6f}')

        # dissimilar sentence
        sample_sent3 = 'Twilight is a bad movie. A total waste of time.'
        token3 = tokenize_text(sample_sent3)
        spl_bow3 = compute_bow(token3, vocab)
        tfidf3 = compute_tf(spl_bow3) * idf
        print('\t Sample sentence 3: ', sample_sent3)
        print(f'\t\t cosine similarity between sentence 1 and sentence 3 = {cosine_similarity(tfidf1, tfidf3):.6f}')

        # show top 5 most similar sentences in the corpus
        print('Top 5 most similar sentences to sentence 1')
        top5 = get_top_5(tfidf, tfidf1)
        for i in top5:
            print('  - ', sentences[i])
    except json.decoder.JSONDecodeError:
        pass