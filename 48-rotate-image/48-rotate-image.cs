public class Solution {
    public void Rotate(int[][] matrix) {
        int temp;     
        for(int i = 0; i < matrix.Length; i++){
            for(int j = matrix[i].Length - 1; j  >= i; j--){
                temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        for(int i = 0; i < matrix.Length; i++){
            Array.Reverse(matrix[i]);
        }
    }
}