class Solution {
  public int solution(int m, int n, String[] board) {
      int answer = 0;
      char[][] field = new char[m][n];
      for(int i = 0; i < m; i++)        //field에 board옮김
      {
          field[i] = board[i].toCharArray();
      }
      boolean[][] visited;  //맞춰진것을 지우기 위함
      boolean end = false;  //지워질 것이 없는지 확인
      
      while(!(end))
      {
          visited = new boolean[m][n];
          end = true;
          for(int i = 0; i < m - 1; i++)
          {
              for(int j = 0; j < n -1; j++)
              {
                  if(field[i][j] == '0')  /*빈 곳은 0으로 채우기 때문에 0이면 통과*/
                      continue;
                  if((field[i][j] == field[i][j+1]) && (field[i][j] == field[i+1][j]) && (field[i][j] == field[i+1][j+1]))  
                      /*자기칸과 오른쪽,아래,대각선칸이 모두같으면 표시*/
                  {
                      visited[i][j] = visited[i][j+1] = visited[i+1][j] = visited[i+1][j+1] = true;
                      end = false;
                  }
              }
          }
          
          for(int i = 0; i < m; i++)    //맞는칸 제거
          {
              for(int j = 0; j < n; j++)
              {
                  if(visited[i][j] == true)
                  {
                      answer++;
                      for(int k = i; k >= 1; k--)   /*위로올라가면서 칸내리기, 원래 있던곳은 0*/
                      {
                          if(field[k-1][j] == '0') break;       //0이면 굳이 칸 움직일 필요 없음
                          field[k][j] = field[k-1][j];
                          field[k-1][j] = '0';
                      }
                  }
              }
          }
      }
      return answer;
  }
}