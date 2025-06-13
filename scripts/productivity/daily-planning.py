#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Daily Planning Script - TDAH Friendly
Automatiza criação do planejamento diário otimizado para TDAH
"""

import datetime
import json
from typing import List, Dict

class DailyPlanner:
    def __init__(self):
        self.energy_levels = {
            "alta": ["05:00-08:00", "14:00-16:00"],
            "media": ["08:00-12:00", "16:00-18:00"],
            "baixa": ["12:00-14:00", "18:00-22:00"]
        }
        
        self.task_types = {
            "criacao": "alta",
            "estrategia": "alta",
            "calls": "alta",
            "trafego": "media",
            "analise": "media",
            "emails": "media",
            "admin": "baixa",
            "organizacao": "baixa"
        }
    
    def create_daily_plan(self, tasks: List[Dict]) -> Dict:
        """
        Cria plano diário otimizado baseado na energia e tipo de tarefa
        """
        plan = {
            "data": datetime.date.today().strftime("%d/%m/%Y"),
            "check_in_matinal": self._generate_checkin(),
            "time_blocks": self._organize_tasks(tasks),
            "lembretes": self._generate_reminders()
        }
        
        return plan
    
    def _generate_checkin(self) -> Dict:
        return {
            "perguntas": [
                "O que é ESSENCIAL hoje?",
                "Qual minha energia atual (1-10)?",
                "Que obstáculos posso antecipar?",
                "Como posso servir através do meu trabalho hoje?"
            ],
            "tempo_estimado": "5 minutos"
        }
    
    def _organize_tasks(self, tasks: List[Dict]) -> Dict:
        organized = {"alta": [], "media": [], "baixa": []}
        
        for task in tasks:
            task_type = task.get("tipo", "admin")
            energy_needed = self.task_types.get(task_type, "media")
            organized[energy_needed].append(task)
        
        return {
            "blocos_alta_energia": {
                "horarios": self.energy_levels["alta"],
                "tarefas": organized["alta"][:2]  # Máximo 2 por bloco
            },
            "blocos_media_energia": {
                "horarios": self.energy_levels["media"],
                "tarefas": organized["media"][:4]
            },
            "blocos_baixa_energia": {
                "horarios": self.energy_levels["baixa"],
                "tarefas": organized["baixa"]
            }
        }
    
    def _generate_reminders(self) -> List[str]:
        return [
            "📱 Modo avião durante deep work",
            "⏰ Timer de 45min + pausa de 15min",
            "💧 Hidratação a cada hora",
            "📝 Capturar ideias imediatamente",
            "🎯 Máximo 3 prioridades por dia",
            "🙏 Pausas para oração/reflexão"
        ]
    
    def export_to_json(self, plan: Dict, filename: str = None) -> str:
        if not filename:
            filename = f"plano_{datetime.date.today().strftime('%Y%m%d')}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(plan, f, ensure_ascii=False, indent=2)
        
        return filename

def main():
    # Exemplo de uso
    planner = DailyPlanner()
    
    # Tarefas exemplo
    tasks_exemplo = [
        {"nome": "Criar conteúdo Instagram", "tipo": "criacao", "tempo": 60},
        {"nome": "Análise métricas tráfego", "tipo": "analise", "tempo": 30},
        {"nome": "Call cliente Gabriele", "tipo": "calls", "tempo": 45},
        {"nome": "Organizar emails", "tipo": "emails", "tempo": 20},
        {"nome": "Planejamento semanal projeto Névoa", "tipo": "estrategia", "tempo": 90}
    ]
    
    # Gerar plano
    plan = planner.create_daily_plan(tasks_exemplo)
    
    # Exportar
    filename = planner.export_to_json(plan)
    print(f"✅ Plano diário gerado: {filename}")
    
    # Mostrar resumo
    print("\n📋 RESUMO DO DIA:")
    print(f"📅 Data: {plan['data']}")
    print(f"🎯 Check-in matinal: {len(plan['check_in_matinal']['perguntas'])} perguntas")
    print(f"⚡ Tarefas alta energia: {len(plan['time_blocks']['blocos_alta_energia']['tarefas'])}")
    print(f"🔄 Tarefas média energia: {len(plan['time_blocks']['blocos_media_energia']['tarefas'])}")
    print(f"📝 Tarefas baixa energia: {len(plan['time_blocks']['blocos_baixa_energia']['tarefas'])}")

if __name__ == "__main__":
    main()