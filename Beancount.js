const countBs = function(s) {
    let count = 0;
    for(let i = 0; i < s.length; i++) {
        if(s.charAt(i) == 'B') {
            count = count+1;
        }
    }
    return count;
  }
  console.log("Count of B's in given String is: ", countBs("Be Good Do Good."));

  
function countChar(s,l) {
    let count = 0;
    for(let i = 0; i < s.length; i++) {
        if (s.charAt(i) == l) {
            count = count +1;
        }
    }
    return count;
}
console.log("Count of given letter in the given string is", countChar("Where there is A will there is a way.",'i'));