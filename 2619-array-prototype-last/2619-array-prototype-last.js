/**
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function() {
    if(this.length===0){
        return -1
    }
    console.log(this[this.length-1]);
    if(this[this.length-1]!=null){
        return this[this.length-1];
    }else if(this[this.length-1]==null){
        return null;
    }
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */