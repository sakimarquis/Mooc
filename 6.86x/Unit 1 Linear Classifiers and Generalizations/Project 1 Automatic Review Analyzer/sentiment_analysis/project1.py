from string import punctuation, digits
import numpy as np
import random

# Part I


#pragma: coderesponse template
def get_order(n_samples):
    try:
        with open(str(n_samples) + '.txt') as fp:
            line = fp.readline()
            return list(map(int, line.split(',')))
    except FileNotFoundError:
        random.seed(1)
        indices = list(range(n_samples))
        random.shuffle(indices)
        return indices
#pragma: coderesponse end


#pragma: coderesponse template
def hinge_loss_single(feature_vector, label, theta, theta_0):
    """
    Finds the hinge loss on a single data point given specific classification
    parameters.

    Args:
        feature_vector - A numpy array describing the given data point.
        label - A real valued number, the correct classification of the data
            point.
        theta - A numpy array describing the linear classifier.
        theta_0 - A real valued number representing the offset parameter.


    Returns: A real number representing the hinge loss associated with the
    given data point and parameters.
    """
    agreement = label * (np.dot(feature_vector, theta) + theta_0)
    hinge_loss = max(0, 1 - agreement)
    return hinge_loss
#pragma: coderesponse end


#pragma: coderesponse template
def hinge_loss_full(feature_matrix, labels, theta, theta_0):
    """
    Finds the total hinge loss on a set of data given specific classification
    parameters.

    Args:
        feature_matrix - A numpy matrix describing the given data. Each row
            represents a single data point.
        labels - A numpy array where the kth element of the array is the
            correct classification of the kth row of the feature matrix.
        theta - A numpy array describing the linear classifier.
        theta_0 - A real valued number representing the offset parameter.


    Returns: A real number representing the hinge loss associated with the
    given dataset and parameters. This number should be the average hinge
    loss across all of the points in the feature matrix.
    """
    agreement = labels * (feature_matrix @ theta + theta_0)
    hinge_loss = np.maximum(0, 1 - agreement)
    return np.mean(hinge_loss)
#pragma: coderesponse end


#pragma: coderesponse template
def perceptron_single_step_update(
        feature_vector,
        label,
        current_theta,
        current_theta_0):
    """
    Properly updates the classification parameter, theta and theta_0, on a
    single step of the perceptron algorithm.

    Args:
        feature_vector - A numpy array describing a single data point.
        label - The correct classification of the feature vector.
        current_theta - The current theta being used by the perceptron
            algorithm before this update.
        current_theta_0 - The current theta_0 being used by the perceptron
            algorithm before this update.

    Returns: A tuple where the first element is a numpy array with the value of
    theta after the current update has completed and the second element is a
    real valued number with the value of theta_0 after the current updated has
    completed.
    """
    epsilon = 10**(-8)
    if label * (feature_vector @ current_theta + current_theta_0) < epsilon:
        current_theta += feature_vector * label
        current_theta_0 += label
    return (current_theta, current_theta_0)
#pragma: coderesponse end


#pragma: coderesponse template
def perceptron(feature_matrix, labels, T):
    """
    Runs the full perceptron algorithm on a given set of data. Runs T
    iterations through the data set, there is no need to worry about
    stopping early.

    NOTE: Please use the previously implemented functions when applicable.
    Do not copy paste code from previous parts.

    NOTE: Iterate the data matrix by the orders returned by get_order(feature_matrix.shape[0])

    Args:
        feature_matrix -  A numpy matrix describing the given data. Each row
            represents a single data point.
        labels - A numpy array where the kth element of the array is the
            correct classification of the kth row of the feature matrix.
        T - An integer indicating how many times the perceptron algorithm
            should iterate through the feature matrix.

    Returns: A tuple where the first element is a numpy array with the value of
    theta, the linear classification parameter, after T iterations through the
    feature matrix and the second element is a real number with the value of
    theta_0, the offset classification parameter, after T iterations through
    the feature matrix.
    """
    n_data = feature_matrix.shape[0]
    n_para = feature_matrix.shape[1]
    theta = np.zeros(n_para)
    theta_0 = 0
    for t in range(T):
        for i in get_order(n_data):
            theta, theta_0 = perceptron_single_step_update(feature_matrix[i],
                                                           labels[i],
                                                           theta,
                                                           theta_0)
    return (theta, theta_0)
#pragma: coderesponse end


#pragma: coderesponse template
def average_perceptron(feature_matrix, labels, T):
    """
    Runs the average perceptron algorithm on a given set of data. Runs T
    iterations through the data set, there is no need to worry about
    stopping early.

    NOTE: Please use the previously implemented functions when applicable.
    Do not copy paste code from previous parts.

    NOTE: Iterate the data matrix by the orders returned by get_order(feature_matrix.shape[0])


    Args:
        feature_matrix -  A numpy matrix describing the given data. Each row
            represents a single data point.
        labels - A numpy array where the kth element of the array is the
            correct classification of the kth row of the feature matrix.
        T - An integer indicating how many times the perceptron algorithm
            should iterate through the feature matrix.

    Returns: A tuple where the first element is a numpy array with the value of
    the average theta, the linear classification parameter, found after T
    iterations through the feature matrix and the second element is a real
    number with the value of the average theta_0, the offset classification
    parameter, found after T iterations through the feature matrix.

    Hint: It is difficult to keep a running average; however, it is simple to
    find a sum and divide.
    """
    n_data = feature_matrix.shape[0]
    n_para = feature_matrix.shape[1]
    theta = np.zeros(n_para)
    theta_0 = 0
    theta_mean = np.zeros(n_para)
    theta_0_mean = 0
    for t in range(T):
        for i in get_order(n_data):
            theta, theta_0 = perceptron_single_step_update(feature_matrix[i],
                                                           labels[i],
                                                           theta,
                                                           theta_0)
            theta_mean += theta/(T*n_data)
            theta_0_mean += theta_0/(T*n_data)
    return (theta_mean, theta_0_mean)
#pragma: coderesponse end


#pragma: coderesponse template
def pegasos_single_step_update(
        feature_vector,
        label,
        L,
        eta,
        current_theta,
        current_theta_0):
    """
    Properly updates the classification parameter, theta and theta_0, on a
    single step of the Pegasos algorithm

    Args:
        feature_vector - A numpy array describing a single data point.
        label - The correct classification of the feature vector.
        L - The lamba value being used to update the parameters.
        eta - Learning rate to update parameters.
        current_theta - The current theta being used by the Pegasos
            algorithm before this update.
        current_theta_0 - The current theta_0 being used by the
            Pegasos algorithm before this update.

    Returns: A tuple where the first element is a numpy array with the value of
    theta after the current update has completed and the second element is a
    real valued number with the value of theta_0 after the current updated has
    completed.
    """
    if label * (feature_vector @ current_theta + current_theta_0) <= 1:
        current_theta =  (1 - eta*L) * current_theta + eta * feature_vector * label
        current_theta_0 = current_theta_0 + eta * label
    else:
        current_theta = (1 - eta*L) * current_theta
    return (current_theta, current_theta_0)

#pragma: coderesponse end


#pragma: coderesponse template
def pegasos(feature_matrix, labels, T, L):
    """
    Runs the Pegasos algorithm on a given set of data. Runs T
    iterations through the data set, there is no need to worry about
    stopping early.

    For each update, set learning rate = 1/sqrt(t),
    where t is a counter for the number of updates performed so far (between 1
    and nT inclusive).

    NOTE: Please use the previously implemented functions when applicable.
    Do not copy paste code from previous parts.

    Args:
        feature_matrix - A numpy matrix describing the given data. Each row
            represents a single data point.
        labels - A numpy array where the kth element of the array is the
            correct classification of the kth row of the feature matrix.
        T - An integer indicating how many times the algorithm
            should iterate through the feature matrix.
        L - The lamba value being used to update the Pegasos
            algorithm parameters.

    Returns: A tuple where the first element is a numpy array with the value of
    the theta, the linear classification parameter, found after T
    iterations through the feature matrix and the second element is a real
    number with the value of the theta_0, the offset classification
    parameter, found after T iterations through the feature matrix.
    """
    n_data = feature_matrix.shape[0]
    n_para = feature_matrix.shape[1]
    theta = np.zeros(n_para)
    theta_0 = 0
    count = 1
    for t in range(T):
        for i in get_order(n_data):
            eta = 1/(count**0.5)
            theta, theta_0 = pegasos_single_step_update(feature_matrix[i],
                                                        labels[i],
                                                        L,
                                                        eta,
                                                        theta,
                                                        theta_0)
            count += 1
    return (theta, theta_0)
#pragma: coderesponse end

# Part II


#pragma: coderesponse template
def classify(feature_matrix, theta, theta_0):
    """
    A classification function that uses theta and theta_0 to classify a set of
    data points.

    Args:
        feature_matrix - A numpy matrix describing the given data. Each row
            represents a single data point.
                theta - A numpy array describing the linear classifier.
        theta - A numpy array describing the linear classifier.
        theta_0 - A real valued number representing the offset parameter.

    Returns: A numpy array of 1s and -1s where the kth element of the array is
    the predicted classification of the kth row of the feature matrix using the
    given theta and theta_0. If a prediction is GREATER THAN zero, it should
    be considered a positive classification.
    """
    epsilon = 10**(-8)
    prediction = feature_matrix @ theta + theta_0
    return np.where(prediction > epsilon, 1, -1)
#pragma: coderesponse end


#pragma: coderesponse template
def classifier_accuracy(
        classifier,
        train_feature_matrix,
        val_feature_matrix,
        train_labels,
        val_labels,
        **kwargs):
    """
    Trains a linear classifier and computes accuracy.
    The classifier is trained on the train data. The classifier's
    accuracy on the train and validation data is then returned.

    Args:
        classifier - A classifier function that takes arguments
            (feature matrix, labels, **kwargs) and returns (theta, theta_0)
        train_feature_matrix - A numpy matrix describing the training
            data. Each row represents a single data point.
        val_feature_matrix - A numpy matrix describing the training
            data. Each row represents a single data point.
        train_labels - A numpy array where the kth element of the array
            is the correct classification of the kth row of the training
            feature matrix.
        val_labels - A numpy array where the kth element of the array
            is the correct classification of the kth row of the validation
            feature matrix.
        **kwargs - Additional named arguments to pass to the classifier
            (e.g. T or L)

    Returns: A tuple in which the first element is the (scalar) accuracy of the
    trained classifier on the training data and the second element is the
    accuracy of the trained classifier on the validation data.
    """
    theta, theta_0 = classifier(train_feature_matrix, train_labels, **kwargs)

    training_preds = classify(train_feature_matrix, theta, theta_0)
    validation_preds = classify(val_feature_matrix, theta, theta_0)

    training_accu = accuracy(training_preds, train_labels)
    validation_accu = accuracy(validation_preds, val_labels)

    return (training_accu, validation_accu)
#pragma: coderesponse end


#pragma: coderesponse template
def extract_words(input_string):
    """
    Helper function for bag_of_words()
    Inputs a text string
    Returns a list of lowercase words in the string.
    Punctuation and digits are separated out into their own words.
    """
    for c in punctuation + digits:
        input_string = input_string.replace(c, ' ' + c + ' ')

    return input_string.lower().split()
#pragma: coderesponse end


#pragma: coderesponse template

#def bag_of_words(texts):
#    """
#    Inputs a list of string reviews
#    Returns a dictionary of unique unigrams occurring over the input
#
#    Feel free to change this code as guided by Problem 9
#    """
#    # Your code here
#    dictionary = {} # maps word to unique index
#    for text in texts:
#        word_list = extract_words(text)
#        for word in word_list:
#            if word not in dictionary:
#                dictionary[word] = len(dictionary)
#    return dictionary

def bag_of_words(texts):
    """
    Inputs a list of string reviews
    Returns a dictionary of unique unigrams occurring over the input

    Feel free to change this code as guided by Problem 9
    """
    f = open('stopwords.txt')
    stopwords = extract_words(f.read())
    f.close()

    dictionary = {} # maps word to unique index
    for text in texts:
        word_list = extract_words(text)
        for word in word_list:
            if word not in dictionary and word not in stopwords:
                dictionary[word] = len(dictionary)
    return dictionary

#pragma: coderesponse end


#pragma: coderesponse template

def extract_bow_feature_vectors(reviews, dictionary):
    """
    Inputs a list of string reviews
    Inputs the dictionary of words as given by bag_of_words
    Returns the bag-of-words feature matrix representation of the data.
    The returned matrix is of shape (n, m), where n is the number of reviews
    and m the total number of entries in the dictionary.

    Feel free to change this code as guided by Problem 9
    """
    # Your code here

    num_reviews = len(reviews)
    feature_matrix = np.zeros([num_reviews, len(dictionary)])

    for i, text in enumerate(reviews):
        word_list = extract_words(text)
        for word in word_list:
            if word in dictionary:
                feature_matrix[i, dictionary[word]] = 1
    return feature_matrix


#def extract_bow_feature_vectors(reviews, dictionary):
#    """
#    Inputs a list of string reviews
#    Inputs the dictionary of words as given by bag_of_words
#    Returns the bag-of-words feature matrix representation of the data.
#    The returned matrix is of shape (n, m), where n is the number of reviews
#    and m the total number of entries in the dictionary.
#
#    Feel free to change this code as guided by Problem 9
#    """
#    num_reviews = len(reviews)
#    feature_matrix = np.zeros([num_reviews, len(dictionary)])
#
#    for i, text in enumerate(reviews):
#        word_list = extract_words(text)
#        for word in word_list:
#            if word in dictionary:
#                if feature_matrix[i, dictionary[word]] == 0:
#                    feature_matrix[i, dictionary[word]] = 1
#                else:
#                    feature_matrix[i, dictionary[word]] += 1
#    return feature_matrix

#pragma: coderesponse end


#pragma: coderesponse template
def accuracy(preds, targets):
    """
    Given length-N vectors containing predicted and target labels,
    returns the percentage and number of correct predictions.
    """
    return (preds == targets).mean()
#pragma: coderesponse end
