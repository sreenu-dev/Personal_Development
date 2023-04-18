function mergeAlternately(word1: string, word2: string): string {
    let output=''
    let maxLen=Math.max(word1.length,word2.length);
    for(let i=0;i<maxLen;i++){
        if(word1[i]!=undefined){
            output+=word1[i]
        }
        if(word2[i]!=undefined){
            output+=word2[i]
        }
    }
    return output;
};

console.log(mergeAlternately("abc","pqr"))