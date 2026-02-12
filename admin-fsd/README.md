# Admin FSD - Next.js + TypeScript 프로젝트

백엔드 개발자를 위한 Next.js 학습 프로젝트입니다.

## 기술 스택

- **Next.js 16** - React 기반 풀스택 프레임워크
- **TypeScript** - 타입 안정성
- **Tailwind CSS** - 유틸리티 기반 CSS 프레임워크
- **ESLint + Prettier** - 코드 품질 및 포맷팅

## 프로젝트 구조

```
admin-fsd/
├── src/
│   ├── app/              # App Router (Next.js 13+)
│   │   ├── api/         # API 라우트 (백엔드 API 역할)
│   │   │   └── hello/   # 예시: GET/POST /api/hello
│   │   ├── layout.tsx   # 공통 레이아웃
│   │   ├── page.tsx     # 홈 페이지 (/)
│   │   └── globals.css  # 전역 스타일
│   └── ...
├── public/              # 정적 파일
├── .env.local.example   # 환경변수 예시
└── package.json
```

## 시작하기

### 1. 의존성 설치

이미 설치되어 있지만, 새로 설치하려면:

```bash
npm install
```

### 2. 환경변수 설정 (선택사항)

```bash
cp .env.local.example .env.local
# .env.local 파일을 열어 필요한 값을 설정하세요
```

### 3. 개발 서버 실행

```bash
npm run dev
```

브라우저에서 [http://localhost:3000](http://localhost:3000)을 열어보세요.

### 4. API 테스트

백엔드 개발자에게 익숙한 REST API를 Next.js에서 만들 수 있습니다:

```bash
# GET 요청
curl http://localhost:3000/api/hello

# POST 요청
curl -X POST http://localhost:3000/api/hello \
  -H "Content-Type: application/json" \
  -d '{"name": "홍길동"}'
```

## 주요 명령어

```bash
npm run dev          # 개발 서버 시작 (hot reload)
npm run build        # 프로덕션 빌드
npm run start        # 프로덕션 서버 시작
npm run lint         # ESLint 실행
npm run format       # Prettier로 코드 포맷팅
npm run format:check # 포맷팅 체크만 수행
```

## 백엔드 개발자를 위한 핵심 개념

### 1. **App Router** (Next.js 13+)
- `src/app` 디렉토리가 라우팅 기반
- 폴더 구조가 곧 URL 경로
- 예: `src/app/about/page.tsx` → `/about`

### 2. **API Routes**
- `src/app/api` 폴더에서 백엔드 API 작성
- Spring의 `@RestController`와 유사한 역할
- 파일명: `route.ts` (GET, POST, PUT, DELETE 등 export)

### 3. **Server Components vs Client Components**
- 기본적으로 모든 컴포넌트는 **Server Component** (서버에서 렌더링)
- `'use client'`를 파일 상단에 추가하면 **Client Component** (브라우저에서 실행)
- Server Component는 백엔드처럼 데이터베이스 직접 접근 가능

### 4. **환경변수**
- `NEXT_PUBLIC_*`: 브라우저에 노출됨 (public API URL 등)
- 그 외: 서버에서만 접근 가능 (DB 비밀번호, API 키 등)

## 학습 자료

- [Next.js 공식 문서](https://nextjs.org/docs)
- [Next.js Learn 튜토리얼](https://nextjs.org/learn) - 추천!
- [React 공식 문서](https://react.dev)
- [TypeScript 핸드북](https://www.typescriptlang.org/docs/handbook/intro.html)

## 다음 단계

1. `src/app/page.tsx`를 수정해서 홈 페이지 커스터마이징
2. `src/app/api/hello/route.ts`를 참고해서 새로운 API 엔드포인트 만들기
3. 새 페이지 만들기: `src/app/about/page.tsx` 생성
4. 데이터 페칭 실습: 외부 API 호출해보기
5. 데이터베이스 연결: Prisma나 Drizzle ORM 추가

---

즐거운 프론트엔드 학습 되세요! 🚀
