function kidsWithCandies(candies: number[], extraCandies: number): boolean[] {
    let maxVal=Math.max(...candies)
    let output:boolean[]=[];
    for(let kid of candies){
        if(kid+extraCandies>=maxVal){
            output.push(true)
        }else{
            output.push(false)
        }
    }
    return output
};