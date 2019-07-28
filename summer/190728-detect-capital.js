/**
 * @param {string} word
 * @return {boolean}
 */
var detectCapitalUse = function(word) {
    if(word === word.toUpperCase()) return true;
    const l = word.toLowerCase();
    if(word === l) return true;
    return word === l[0].toUpperCase() + l.slice(1);
};