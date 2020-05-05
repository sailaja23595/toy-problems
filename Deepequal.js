const object1 = {
    name1: 'deep',
    name2: 'equal'
}
const object2 = {
   name1: 'deep',
   name2: 'equal'
}

function isObject(obj) {
   if(typeof obj === "object" && obj != null) {
       return true;
   } else {
       return false;
   }
}

function deepEqual(val1, val2) {
   if(val1 == val2) {
       return true;
   } else if (isObject(val1) && isObject(val2)) {
       if(Object.keys(val1).length != Object.keys(val2).length) return false;
       for(let i in object1) {
           if(!deepEqual(val1[i], val2[i])) {
               return false;
           }
       }
       return true;
   } else {
       return false;
   }
}

console.log(deepEqual(object1, object2))
console.log(deepEqual(4, 6))
console.log(deepEqual(6,"6"))