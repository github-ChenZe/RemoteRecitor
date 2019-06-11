function shuffle(array) {
    array.sort(() => Math.random() - 0.5);
}

alphas = ['A', 'B', 'C', 'D'];
alphasToIndex = {'A': 0, 'B': 1, 'C': 2, 'D': 3};

subindex = ['〇', '①', '②', '③', '④'];
    
function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
}