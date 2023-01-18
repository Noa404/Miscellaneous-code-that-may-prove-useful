# git clone github.com/asugden/duq_ds3_2023.git github.com/Noa404/DTSC_300.git

# git status
# git add shows the new file

class generarlCLassifier():
    def __init__(self, train_test_ratio: float) -> None:
        """A general classifier that can be subclassed

        Args:
            train_test_ratio (float): ratio of train set
            to test set
            """
        self.train_test_ratio = train_test_ratio
        self.x = 1
        self.y = 2
        #These have to be after the __init__ statement

    def train(self, data, labels) -> None:
        pass
        #method is a function in a class

    def predict(self, data) -> np.ndarray:
        pass