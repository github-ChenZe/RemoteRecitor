var indexes = [];
function initIndex() {
    indexes = []
    indexes.cursor = -1;
    indexes.getDir = function() {
        return indexes[indexes.cursor]['dir'];
    }
    indexes.gotRight = function() {
        if (indexes[indexes.cursor]['status'] == 'unanswered')
            indexes[indexes.cursor]['status'] = 'correct';
    }
    indexes.gotWrong = function() {
        if (indexes[indexes.cursor]['status'] == 'unanswered')
            indexes[indexes.cursor]['status'] = 'wrong';
    }
}

function setIndex(list) {
    for (var i = 0; i < list.length; i++) {
        indexes.push(list[i]);
        indexes[i]['status'] = 'unanswered';
    }
}

function countCorrect() {
    var correct = 0;
    for (var i = 0; i < indexes.length; i++) {
        if (indexes[i]['status'] == 'correct') {
            correct++;
        }
    }
    return correct;
}

function countTotal() {
    return indexes.length;
}

function allUnansweredToWrong() {
    for (var i = 0; i < indexes.length; i++) {
        if (indexes[i]['status'] == 'unanswered') {
            indexes[i]['status'] = 'wrong'
        }
    }
}

function allDone() {
    var allDone = true;
    for (var i = 0; i < indexes.length; i++) {
        if (indexes[i]['status'] == 'unanswered') {
            allDone = false;
        }
    }
    return allDone;
}