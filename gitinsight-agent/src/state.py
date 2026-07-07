from typing import TypedDict, List, Dict, Any

class InterviewState(TypedDict):
    """
    GitInsight Agent의 전역 상태(State)를 관리하는 스키마입니다.
    """
    user_id: str                 # 이용자 식별 ID
    repo_url: str                # 입력받은 GitHub 레포지토리 주소
    repo_commit_hash: str        # 캐시 검증용 최신 커밋 해시 값
    tech_stack: List[str]        # 추출된 프로젝트 주요 기술 스택 리스트
    extracted_chunks: List[Dict[str, Any]]  # 선별된 상위 코드/족보 청크 리스트
    current_question: str        # AI 면접관이 유저에게 던진 현재 질문
    answer_history: List[str]    # 유저 답변 누적 히스토리
    loop_count: int              # 압박 질문 최대 3회 제한 카운터 (0~3)
    is_answer_sufficient: bool   # 유저 답변의 통과/미달 여부 플래그
    evaluation: Dict[str, Any]   # 기술 면접 루브릭 평가 결과 데이터
    final_report: str            # 최종 리팩토링 리포트 텍스트
