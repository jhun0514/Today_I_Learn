# Algorithm

* [BFS](https://github.com/jhun0514/Today_I_Learn/blob/master/Algorithm/BFS.md)
<!-- * [멀티스레드](#멀티-스레드)
  * 장점과 단점
  * 멀티스레드 vs 멀티프로세스 -->

[뒤로](https://github.com/jhun0514/Today_I_Learn)

</br>

---

</br>
<!--
---

## 스케줄러

_프로세스를 스케줄링하기 위한 Queue 에는 세 가지 종류가 존재한다._

* Job Queue : 현재 시스템 내에 있는 모든 프로세스의 집합
* Ready Queue : 현재 메모리 내에 있으면서 CPU 를 잡아서 실행되기를 기다리는 프로세스의 집합
* Device Queue : Device I/O 작업을 대기하고 있는 프로세스의 집합

각각의 Queue 에 프로세스들을 넣고 빼주는 스케줄러에도 크게 **세 가지 종류가** 존재한다.

### 장기스케줄러(Long-term scheduler or job scheduler)

메모리는 한정되어 있는데 많은 프로세스들이 한꺼번에 메모리에 올라올 경우, 대용량 메모리(일반적으로 디스크)에 임시로 저장된다. 이 pool 에 저장되어 있는 프로세스 중 어떤 프로세스에 메모리를 할당하여 ready queue 로 보낼지 결정하는 역할을 한다.

* 메모리와 디스크 사이의 스케줄링을 담당.
* 프로세스에 memory(및 각종 리소스)를 할당(admit)
* degree of Multiprogramming 제어  
  (실행중인 프로세스의 수 제어)
* 프로세스의 상태  
  new -> ready(in memory)

_cf) 메모리에 프로그램이 너무 많이 올라가도, 너무 적게 올라가도 성능이 좋지 않은 것이다. 참고로 time sharing system 에서는 장기 스케줄러가 없다. 그냥 곧바로 메모리에 올라가 ready 상태가 된다._

</br>

### 단기스케줄러(Short-term scheduler or CPU scheduler)

* CPU 와 메모리 사이의 스케줄링을 담당.
* Ready Queue 에 존재하는 프로세스 중 어떤 프로세스를 running 시킬지 결정.
* 프로세스에 CPU 를 할당(scheduler dispatch)
* 프로세스의 상태  
  ready -> running -> waiting -> ready

</br>

### 중기스케줄러(Medium-term scheduler or Swapper)

* 여유 공간 마련을 위해 프로세스를 통째로 메모리에서 디스크로 쫓아냄 (swapping)
* 프로세스에게서 memory 를 deallocate
* degree of Multiprogramming 제어
* 현 시스템에서 메모리에 너무 많은 프로그램이 동시에 올라가는 것을 조절하는 스케줄러.
* 프로세스의 상태  
  ready -> suspended

#### Process state - suspended

Suspended(stopped) : 외부적인 이유로 프로세스의 수행이 정지된 상태로 메모리에서 내려간 상태를 의미한다. 프로세스 전부 디스크로 swap out 된다. blocked 상태는 다른 I/O 작업을 기다리는 상태이기 때문에 스스로 ready state 로 돌아갈 수 있지만 이 상태는 외부적인 이유로 suspending 되었기 때문에 스스로 돌아갈 수 없다.

[뒤로](https://github.com/JaeYeopHan/for_beginner)/[위로](#part-1-4-운영체제)

</br>

---
-->
