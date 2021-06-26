# Part 1-2 Common Sense of Development

* [GitFlow](#GitFlow)
* [PR 코드리뷰](#PR-코드리뷰)

[뒤로](https://github.com/jhun0514/Today_I_Learn)

</br>

---

## GitFlow

- 의미: 깃플로우 전략은 소스코드 관리 및 출시를 위한 브랜치 관리 전략 중 하나이다.
- 브랜치 종류:
  * 메인브렌치(항상 유지):
    * Master - 제품으로 출시 되는 브랜치
    * Develop - 다음 출시 버전을 개발하는 브랜치
  * 보조 브랜치(일정기간 유지):
    * Feature - 기능을 개발하는 브랜치
    * Realease - 이번 출시 버전을 준비하는 브랜치
    * HotFix - 출시 버전에서 발생한 버그를 수정하는 브랜치

[뒤로](https://github.com/jhun0514/Today_I_Learn)/[위로](#part-1-2-Common-Sense-of-Development)/[참고자료](https://mishka.kr/2020/03/30/gitflow/)

</br>

---

## PR 코드리뷰

- 의미: 협업 할 때 가장 중요한 기능으로 브랜치 Merge 전 확인을 받는 절차이다.
- 특징:
  * Reviewers: 현재 PR을 리뷰 해 줄 팀원을 지정한다.
  * Assignees: 현재 PR 담장자를 지정해주면 된다.
- 리뷰 종류:
  * Comment: 승인과 무관하게 일반적 커멘트
  * Approve: 리뷰어가 승인하는 것으로 머지해도 괜찮다는 의견을 보내는 것이다.
  * Request Changes: 변경 요청으로 승인을 거부하는 것이다.

[뒤로](https://github.com/jhun0514/Today_I_Learn)/[위로](#part-1-2-Common-Sense-of-Development)/[참고자료](https://mishka.kr/2020/03/30/gitflow/)

</br>

---
