# GB10 상시 운영 구성 (2026-11-12)

실험 장비를 다른 기기에서 API로 쓰는 상시 서버로도 운영하기 위한 구성입니다. 스크립트는 GB10의 `~/llm/` 아래에 있고 저장소에는 넣지 않습니다(호스트 주소·키 경로 포함).

## 배경

- 측정 첫날 Wi-Fi 끊김(SSH 1회)과 DGX Dashboard 시스템 업데이트 후 재부팅이 각각 한 번 있었습니다. 재부팅 후 수동으로 띄운 서버가 돌아오지 않아 한 실험 묶음이 전부 `Connection refused`로 실패했습니다.
- 유선 연결은 쓸 수 없는 환경입니다.
- GB10에는 `unattended-upgrades`가 설치되어 있지 않아, 저절로 패키지를 설치하거나 재부팅하는 경로는 없습니다. 재부팅은 Dashboard·apt에서 사람이 업데이트를 적용할 때 생깁니다.

## 자동 재시작 (사용자 systemd, sudo 불필요)

| 구성 요소 | 역할 |
|---|---|
| `loginctl enable-linger` | 로그인하지 않아도 부팅 시 사용자 서비스 실행 |
| `~/llm/serve-mode` | 기본 서버 선택: `vllm` / `strata` / `none`(실험 중) |
| `llm-serve.service` | 부팅 시 Tailscale 주소가 잡힐 때까지 최대 5분 기다린 뒤 선택한 서버를 시작 |
| `llm-serve-check.timer` | 부팅 10분 후부터 5분마다 `/v1/models` 확인, 응답이 없으면 재시작 |
| vLLM 컨테이너 | Docker 재시작 정책을 `no`로 바꾸고 시작을 서비스에 맡김 (Tailscale보다 먼저 떠서 포트 바인딩에 실패하는 경쟁 상태 방지) |
| Strata | `strata launch --preset gb10-default`로 시작 (preset은 기본 모드 전환 시 저장) |

실험할 때는 `echo none > ~/llm/serve-mode`로 두고, 끝나면 `vllm` 또는 `strata`로 되돌립니다. 측정 중 자동 재시작이 끼어들지 않게 하기 위해서입니다.

## 관리자 설정 (`sudo bash ~/llm/admin-setup.sh`, 1회)

1. 사용 중인 Wi-Fi 연결의 절전 끄기 (`802-11-wireless.powersave 2`)
2. snap 자동 갱신을 일요일 04:00~05:00으로 제한
3. apt: 패키지 목록만 내려받고 자동 설치·자동 재부팅은 하지 않음 (`/etc/apt/apt.conf.d/99-gb10-llm-server`)

권장 운영: 업데이트는 일요일 04:00~05:00에 Dashboard나 apt로 직접 적용합니다. 재부팅되면 `llm-serve`가 기본 서버를 다시 띄웁니다.

## 검증 상태

- 서비스 등록과 `none` 모드 동작은 확인했습니다.
- **재부팅 후 자동 복구는 아직 실제 재부팅으로 시험하지 않았습니다.** 실험이 끝나고 기본 모드를 정한 뒤 확인합니다.
