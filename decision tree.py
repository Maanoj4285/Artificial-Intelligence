import numpy as np
import pandas as pd

class DecisionTree:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth
        self.tree = None

    def entropy(self, y):
        unique_counts = np.bincount(y)
        probabilities = unique_counts / len(y)
        return -np.sum([p * np.log2(p) for p in probabilities if p > 0])

    def information_gain(self, X, y, feature):
        total_entropy = self.entropy(y)
        values, counts = np.unique(X[:, feature], return_counts=True)
        weighted_entropy = np.sum(
            [(counts[i] / np.sum(counts)) * self.entropy(y[X[:, feature] == values[i]]) for i in range(len(values))])
        return total_entropy - weighted_entropy

    def best_split(self, X, y):
        best_feature = -1
        best_info_gain = -1
        for feature in range(X.shape[1]):
            info_gain = self.information_gain(X, y, feature)
            if info_gain > best_info_gain:
                best_info_gain = info_gain
                best_feature = feature
        return best_feature

    def build_tree(self, X, y, depth):
        if len(np.unique(y)) == 1:
            return int(y[0])
        if X.shape[1] == 0 or (self.max_depth is not None and depth >= self.max_depth):
            return int(np.argmax(np.bincount(y)))

        best_feature = self.best_split(X, y)
        if best_feature == -1:
            return int(np.argmax(np.bincount(y)))

        tree = {int(best_feature): {}}
        values = np.unique(X[:, best_feature])
        for value in values:
            sub_X = X[X[:, best_feature] == value]
            sub_y = y[X[:, best_feature] == value]
            sub_tree = self.build_tree(np.delete(sub_X, best_feature, axis=1), sub_y, depth + 1)
            tree[int(best_feature)][int(value)] = sub_tree
        return tree

    def fit(self, X, y):
        self.tree = self.build_tree(X, y, 0)

    def predict_one(self, x, tree):
        if not isinstance(tree, dict):
            return tree
        feature = next(iter(tree))
        value = x[feature]
        if value in tree[feature]:
            return self.predict_one(x, tree[feature][value])
        else:
            return int(max(set(y), key=list(y).count))  # Default to most common label if missing value in tree

    def predict(self, X):
        return [self.predict_one(x, self.tree) for x in X]


# Example usage:
if __name__ == "__main__":
    # Example dataset: Play Tennis
    data = {
        'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain', 'Sunny',
                    'Overcast', 'Overcast', 'Rain'],
        'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild',
                        'Hot', 'Mild'],
        'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal', 'Normal',
                     'High', 'Normal', 'High'],
        'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong',
                 'Strong', 'Weak', 'Strong'],
        'PlayTennis': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
    }

    df = pd.DataFrame(data)
    X = df[['Outlook', 'Temperature', 'Humidity', 'Wind']].apply(lambda col: pd.factorize(col, sort=True)[0]).values
    y = df['PlayTennis'].apply(lambda label: 1 if label == 'Yes' else 0).values

    tree = DecisionTree(max_depth=3)
    tree.fit(X, y)
    predictions = tree.predict(X)

    print("Predictions:", [int(pred) for pred in predictions])
    print("Actual:     ", y.tolist())
    print("Tree:       ", tree.tree)
