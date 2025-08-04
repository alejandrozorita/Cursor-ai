#!/usr/bin/env python3
"""
Script de inicio para la aplicación FastAPI
Permite ejecutar la aplicación en diferentes modos
"""

import argparse
import uvicorn
import sys
import os

def main():
    parser = argparse.ArgumentParser(description="Iniciar la aplicación FastAPI")
    parser.add_argument(
        "--host", 
        default="0.0.0.0", 
        help="Host donde ejecutar la aplicación (default: 0.0.0.0)"
    )
    parser.add_argument(
        "--port", 
        type=int, 
        default=8000, 
        help="Puerto donde ejecutar la aplicación (default: 8000)"
    )
    parser.add_argument(
        "--reload", 
        action="store_true", 
        help="Habilitar recarga automática en desarrollo"
    )
    parser.add_argument(
        "--workers", 
        type=int, 
        default=1, 
        help="Número de workers (default: 1)"
    )
    parser.add_argument(
        "--log-level", 
        default="info", 
        choices=["debug", "info", "warning", "error", "critical"],
        help="Nivel de logging (default: info)"
    )

    args = parser.parse_args()

    print(f"🚀 Iniciando FastAPI en http://{args.host}:{args.port}")
    print(f"📚 Documentación disponible en http://{args.host}:{args.port}/docs")
    print(f"🔄 Modo reload: {'Activado' if args.reload else 'Desactivado'}")
    print(f"👥 Workers: {args.workers}")
    print(f"📝 Log level: {args.log_level}")
    print("-" * 50)

    try:
        uvicorn.run(
            "main:app",
            host=args.host,
            port=args.port,
            reload=args.reload,
            workers=args.workers,
            log_level=args.log_level
        )
    except KeyboardInterrupt:
        print("\n👋 Aplicación detenida por el usuario")
    except Exception as e:
        print(f"❌ Error al iniciar la aplicación: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 