## [DP] 왼쪽 맞춤
-------------
- 아래한글이나 MS 워드에서는 문단을 왼쪽맞춤, 오른쪽맞춤, 양쪽맞춤 중 하나로 편집가능하다. 그 중에서 **왼쪽맞춤**을 생각해보자
    - 각 줄의 처음은 단어로 시작하고, 두 단어 사이에는 정확히 하나의 공백(space)을 넣는다고 가정한다
    - 단어 하나는 반드시 한 줄에 포함되어야 한다. 즉, 두 줄에 걸쳐 나뉘어 나타나지 않아야 한다
- 문장을 페이지 폭이 `W`인 쪽(page)에서 왼쪽 맞춤을 예쁘게 하기 위해, 각 줄마다 penalty 점수를 `(W - 해당 줄의 글자 수 - 단어 사이의 공백 수)**3 `으로 정의한다
    - 예: `Ape ate apple.`   에서 `W = 16`이고, `글자수 = 12` (마침표 포함), `세 단어 사이의 공백 수 = 2`이므로 `(16 - 14)**3 = 2**3 = 8` 점이 penalty 값이다 (여기서 가장 뒤 초록색과 보라색은 오른쪽 끝에 남은 공백이다!)

- **최종 왼쪽 맞춤의 penalty 값은 각 줄의 penalty 값의 합**으로 정의된다
- **입력:**  W값을 첫 번째 줄에서 먼저 입력받고 두 번째 줄에서 여러 문장을 <u>**한 줄**</u>로 입력받는다.
입력 받은 문장을 공백을 기준으로 `split`으로 분할하여, 폭이 W인 페이지에 왼쪽맞춤을 하는데, penalty 값이 최소가 되도록 한다. (DP로 해결 가능)
단, W 값은 가장 긴 단어(구둣점 포함)의 길이보다 같거나 크다고 가정해도 된다
- **출력:** <u>**최소 penalty**</u> 값이다
- **분석:** 코드 마지막에 주석으로 DP 점화식을 쓰고 알고리즘의 수행시간을 간단하게 분석한 후 Big-O 기호로 표기할 것
- **[주의]** 유사도 검사를 실시할 예정이니 꼭 혼자 힘으로 짜보길 바랍니다!
