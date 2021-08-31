# Part 5-2 Spring

* [Spring Boot](#Spring-Boot)
* [Thymeleaf vs jsp](#Thymeleaf-vs-jsp)
* [Spring Boot Devtools](#Spring-Boot-Devtools)
* [Spring DI](#Spring-DI)
* [스프링 데이터베이스 접근 기술](#스프링-데이터베이스-접근-기술)
* [RestTemplate](#RestTemplate)
* [HTTP Methods for RESTful Service](#HTTP-Methods-for-RESTful-Service)
* [Entity](#Entity)

[뒤로](https://github.com/jhun0514/Today_I_Learn)

</br>

---

## Spring Boot

- 사전지식: 스프링 프레임워크는 자바기반 엔터프라이즈 애플리케이션 개발을 위한 포괄적인 인프라를 제공해주는 플랫폼이다.
- 역할: 스프링 부트는 실행만 하면 스프링 기반의 상용화가 가능한 애플리케이션을 쉽게 만들기 위해 단독 실행을 가능하게 해주는 스프링 프로젝트이다. 즉, 스프링부트는 스프링을 쉽게 사용할 수 있도록 필요한 설정을 대부분 미리 세팅해 놓았다는 뜻이다.
- 특징:
  * 단독으로 실행 가능한 스프링 애플리케이션을 생성한다.
  * Tomcat, Jetty, Undertow를 내장한다. (내장 웹 서버들)
  * 기본설정이 되어있는 starter 컴포넌트 제공
  * 가능한 자동으로 설정되어 있다
  * 상용화에 필요한 통계, 상태 체크,외부 설정 등을 제공
  * 설정을 위한 XML 코드를 생성하거나 요구하지 않음

[뒤로](https://github.com/jhun0514/Today_I_Learn)/[위로](#part-5-2-Spring)/[참고자료](https://noahlogs.tistory.com/46)

</br>

---

## Thymeleaf vs jsp

### Thymeleaf
- 역할: 템플릿 엔진으로 스프링 프레임워크의 MVC구조에서 V(view)를 담당하는 라이브러리 입니다.
- 특징:
  * HTML, XML, Javascript, CSS 및 일반 텍스트를 처리 할 수 있는 웹 및 독립형 환경에서 사용할 수 있는 JAVA 템플릿 엔진이다.
  * HTML파일을 가져와서 파싱해서 분석 후 정해진 위치에 데이터를 치환해서 웹페이지를 생성한다.
  * 자바 코드를 뷰 내에서 사용할 수 없다.

### jsp
- 역할: 스프링 프레임워크의 뷰로 사용되는 가장 일반적인 기술
- 특징:
  * 서블릿으로 변환되어 실행이 되어진다.
  * JSP내에서 자바 코드를 사용할 수 있다.
  * 커스텀 태그 기능이 있다.

### 장단점
- JSP는 서블릿이다 보니 뭐든지 할 수 있다는게 장점이자 단점이다. MVC 구조가 주로 사용되며 JSP는 뷰만 담당하고, JSP에 비지니스 로직을 넣으면 디버깅 및 유지보수가 힘들어진다 하여 요즘은 JSP에서 자바코드를 사용하지 못하게 하는게 일반적이다. JSP를 웹브라우저로 열어보면 제대로 된 모양이 보이지 않는다.
- Thymeleaf 엔진은 페이지를 생성하는데 필요한 정보를 태그의 속성으로 넣고, remove속성을 이용해서 실제 생성될 페이지에서는 제거될 태그를 넣을 수 있어서 페이지의 프로토 타입을 제공할 수 있다는 것입니다. Thymeleaf로 작성된 페이지를 웹 브라우저에서 열어보면 실제 보여질 내용과 동일하게 보여진다. 또한 디자이너가 페이지를 생성 및 수정 할때 톰캣같은 웹서버를 실행하지 않고 오프라인에서 수정을 할 수 가 있다는 장점이 있다.
- 속도는 Thymeleaf가 대부분의 템플릿 엔진에 비해 느리다.

[뒤로](https://github.com/jhun0514/Today_I_Learn)/[위로](#part-5-2-Spring)

</br>

---

## Spring Boot Devtools

- 기능은 크게 5가지 이다.
  * Property Defaults
  * Automatic Restart
  * Live Reload
  * Global Setting
  * Remote Applications

### Property Defaults
- 스프링의 타임리프는 기본적으로 캐싱 기능을 사용한다. 하지만 개발과전에서 캐싱이 되어 있다면, 우리가 타임리프 파일을 수정하더라도, 반영되지 않는다. 따라서 어플리케이션 캐시 설정값을 false로 수정해야 한다. 이러한 작업을 Property Defaults 가 제공한다. 개발 시점과 배포시점에 다른 설저을 기본적으로 개발 단계에 맞춰 설정해준다.

### Automatic Restart
- 개발하다 보면 어플리케이션을 재시작해야 하는 경우가 많다. 이기능을 자동으로 제공해주는 것인데 파일 수정 후 저장을 하면 classpath에 존재하는 파일의 변경을 감지하고 자동으로 서버를 restart해준다.

### Live Reload
- 파일을 수정하기만 해도 자동으로 브라우저가 새로 고침 되는 기능이다. 내부적으로 live reload 서버를 두고 브라우저 확장프로그램과 통신하는 방식으로 동작한다.

[뒤로](https://github.com/jhun0514/Today_I_Learn)/[위로](#part-5-2-Spring)/[참고자료](https://velog.io/@bread_dd/Spring-Boot-Devtools)

</br>

---

## Spring DI

- 의미: IOC(Inversion of Control)의 일종으로 의존 관계 주입이라고한다. 어떤 객체가 사용하는 의존 객체를 직접 만드는 것이아닌 주입 받아 사용한다.
- 사용이유:
  * 재사용성을 높여준다.
  * 테스트에 용이하다.
  * 코드를 단순화 시켜준다.
  * 사용하는 이유를 파악하기 수월하고 코드가 읽기 쉬워진다.
  * 종속성이 감소하기 때문에 변경에 민감하지 않다.
  * 결합도는 낮추면서 유연성과 확장성은 향상 시킬 수 있다.
  * 객체간의 의존관계를 설정할 수 있다.

### 직접 Bean 등록
- 스프링 IoC 컨테이너가 관리하는 객체이다.
- 의존성 관리가 수월해진다.
- 싱글톤 형태이(하나의 빈 정의에 대해서 컨테이너 내에 단 하나의 객체만 존재한다.)
- 하나 하나 등록해야 하기에 번거로움이 있다.

### Component 스캔과 자동 의존관계 설정
- Component 애노테이션이 있으면 빈으로 자동 등록된다.
- Controller, Service, Repository 등은 컴포넌트를 포함하기에 빈으로 자동등록된다.

### Autowired
- 생성자에 Autowired 애노테이션을 붙이면 객체 생성 시점에 해당 빈을 찾아 주입한다.
- 생성자가 1개라면 생략가능하다.
- 필드, 새터 등에도 주입한다.

### SpringBootApplication
- ComponentScan(패키지 아래에 있는 빈으로 등록해야할 어노테이션을 찾아 전부 빈으로 등록해준다.) 등 여러가지 기능이 포함된다.

[뒤로](https://github.com/jhun0514/Today_I_Learn)/[위로](#part-5-2-Spring)/[참고자료](https://chanhuiseok.github.io/posts/spring-5/)/[참고자료](https://devlog-wjdrbs96.tistory.com/165)

</br>

---

## 스프링 데이터베이스 접근 기술

- 종류: 크게 4가지가 있다.
  * JDBC
  * JDBC Template
  * JPA
  * Spring JPA

### JDBC
- jdbc란 자바 언어로 다양한 종류의 관계형 데이터베이스에 접속할 수 있도록 하는 자바 API이다.
- jdbc는 데이터베이스에서 자료를 쿼리하거나 업데이트 하는 방법을 제공한다.
- 옛날에는 jdbc api로 직접 코딩을 하였다고 한다. 코드의 양이 굉장히 많고 반복되는 코드가 존재했다.

### JDBC Template
- Jdbc Template 이나 MyBatis 와 같은 라이브러리를 통해 기존의 jdbc api의 반복 코드 대부분을 제거해 줘서 좀 더 쉽게 사용할 수 있게 되었다.
- 그러나 SQL은 직접 작성해야 한다.

### JPA
- JPA는 기존의 반복 코드는 물론이고, 기본적인 SQL도 JPA가 직접 만들어서 실행해준다.
- JPA를 사용하면, SQL과 데이터 중심의 설계에서 객체 중심의 설계로 패러다임을 전환을 할 수 있다.
- JPA를 사용하면 개발 생산성을 크게 높일 수 있다.

### Spring JPA
- 구현 클래스 없이 인터페이스 만으로 개발을 완료할 수 있습니다.
- 반복 개발해온 기본 CRUD 기능도 스프링 데이터 JPA가 모두 제공합니다.
- 스프링 데이터 JPA는 JPA를 편리하게 사용하도록 도와주는 기술입니다.

[뒤로](https://github.com/jhun0514/Today_I_Learn)/[위로](#part-5-2-Spring)/[참고자료](https://chanhuiseok.github.io/posts/spring-5/)

</br>

---

## RestTemplate

- 의미: 스프링 프레임워크에서는 REST 서비스의 Endpoint를 호출할 수 있도록 크게 동기, 비동기 REST Client 를 제공하는데 RestTemplate은 동기방식이다.

### 특징
- REST API 호출이후 응답을 받을 때까지 기다리는 동기방식이다.
- 다른 여러 Template 클래스와 동일한 원칙에 따라 설계되어 단순한 방식의 호출로 복잡한 작업을 쉽게 하도록 제공한다.
- REST 서비스를 호출하도록 설계되어 HTTP 프로토콜의 메서드 (GET, POST, DELETE, PUT)에 맞게 여러 메서드를 제공한다.

### 그외
- AsyncRestTemplate
  * 비동기 RestTemplate 이다.
- WebClient
  * 논블럭, 리엑티브 웹 클라이언트로 동기, 비동기 방식을 지원한다.

[뒤로](https://github.com/jhun0514/Today_I_Learn)/[위로](#part-5-2-Spring)/[참고자료](https://advenoh.tistory.com/46)

</br>

---

## HTTP Methods for RESTful Service

- 의미: HTTP 문법은 정규화 인터페이스로 구성되어 있고 명사 단위 소스에 대응하도록 되어있다. 기본적인 CRUD를 구현하며 이외 다른 문법들도 제공한다.

### CRUD 문법
- POST (Create): 새로운 데이터를 만드는데 사용한다. 새로운 URL을 위해 ID를 부여하며 성공시 201를 리턴, 에러시 409(중복), 404(not found)를 리턴한다.
- GET (Read): 데이터를 읽는데 사용한다. 에러가 없으면 XML이나 JSON으로 200코드와 함께 리턴한다. 에러시 404(not found), 400(bad request) 리턴한다.
- PUT (Update/Replace): 데이터를 업데이트 하는데 사용한다. 존재하는 데이터에 PUT을 사용하면 새로운 데이터가 업데트된다. 존재하지 않는 데이터에 PUT을 사용하면 새로운 데이터가 생성된다 이런 경우 URL ID는 생성되지 않는다. 에러가 없으면 200코드와 함께 리턴한다 (204 바디가 없을시). 에러시 404(not found), 405(method not allowed) 리턴한다.
- PATCH (Update/Modify): 데이터를 수정 하는데 사용한다. 수정 이므로 완벽한 데이터가 필요하지 않다. 에러가 없으면 200코드와 함께 리턴한다 (204 바디가 없을시). 에러시 404(not found), 405(method not allowed) 리턴한다.
- DELETE (Delete): 데이터를 삭제하는데 사용한다. 에러가 없으면 200코드와 함께 리턴한다 (204 바디가 없을시). 에러시 404(not found), 405(method not allowed) 리턴한다.

[뒤로](https://github.com/jhun0514/Today_I_Learn)/[위로](#part-5-2-Spring)/[참고자료](https://www.restapitutorial.com/lessons/httpmethods.html)

</br>

---

## Entity

- 의미: MVC기반으로 개발하며 REST API 서버를 만들때 Data model을 분리해서 사용하는게 일반적이며 '@Entity' 어노테이션을 붙여 DB테이블 구조의 역할을 부여한다. Model 역할을 하는 클래스이다.

- 특징: 영속성 모델을 기반으로 만들어진 Entity는 테이블이 변경될때 필연적으로 변경이 일어나는 클래스이고 그에 따른 영향의 범위는 Model 영역 내에서만 이어야 한다.

### Main Annotation
- '@Entity': 해당 클래스가 entity임을 명시
- '@Table': 실제 DB테이블의 이름을 명시
- '@Id': Index primary key를 명시
- '@Column': 실제 DB Column을 명시
- '@GeneratedValue': Primary key 식별키의 전략 설정

[뒤로](https://github.com/jhun0514/Today_I_Learn)/[위로](#part-5-2-Spring)/[참고자료](https://yonguri.tistory.com/69)

</br>

---
