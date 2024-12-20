# Flask App с метриками Prometheus

Этот проект представляет собой веб-приложение на Flask, оснащённое метриками Prometheus для мониторинга и анализа производительности. Оно предоставляет ключевые метрики, такие как количество запросов и задержка, которые собираются и визуализируются с помощью Prometheus и Grafana.

## Основные возможности

- **Flask API**: Простое Flask-приложение с API эндпоинтами.
- **Метрики Prometheus**: Предоставляет эндпоинт `/metrics` для мониторинга ключевых показателей.
- **Middleware**: Отслеживает количество запросов, задержку и HTTP-статусы.
- **Интеграция**: Совместимо с Prometheus и Grafana для мониторинга в реальном времени.

## Содержание

- [Установка](#установка)
- [Конфигурация](#конфигурация)
- [Использование](#использование)
- [Интеграция с Prometheus](#интеграция-с-prometheus)
- [Настройка Grafana](#настройка-grafana)
- [Доступные метрики](#доступные-метрики)
- [Вклад в проект](#вклад-в-проект)
- [Лицензия](#лицензия)

---


## Конфигурация

Обновите конфигурацию приложения в файле `swagger/swagger.yaml` по мере необходимости. Убедитесь, что конфигурация вашего сервера Prometheus включает цель:

```yaml
scrape_configs:
  - job_name: 'flask_app'
    static_configs:
      - targets: ['localhost:8080']
```

---

## Использование

### Запуск приложения

```bash
python app.py
```

Приложение будет доступно по адресу [http://localhost:8080](http://localhost:8080).

### API эндпоинты

- `/`: Возвращает простое сообщение.
- `/metrics`: Предоставляет метрики Prometheus для мониторинга.

---

## Интеграция с Prometheus

1. Установите и настройте Prometheus ([руководство по установке](https://prometheus.io/docs/introduction/first_steps/)).
2. Обновите ваш файл `prometheus.yml` следующим образом:

   ```yaml
   scrape_configs:
     - job_name: 'flask_app'
       static_configs:
         - targets: ['localhost:8080']
   ```

3. Запустите Prometheus и проверьте цель по адресу [http://localhost:9090/targets](http://localhost:9090/targets).

---

## Настройка Grafana

1. Установите Grafana ([руководство по установке](https://grafana.com/docs/grafana/latest/installation/)).
2. Добавьте Prometheus как источник данных в Grafana:
   - Перейдите в **Configuration** → **Data Sources** → **Add data source**.
   - Выберите **Prometheus**.
   - Укажите URL `http://localhost:9090`.
   - Нажмите **Save & Test**.
3. Импортируйте готовую панель или создайте свою для визуализации метрик.

---

## Доступные метрики

### Пользовательские метрики

1. **Количество запросов** (`flask_app_request_count`):
   - Метки:
     - `method`: HTTP-метод (`GET`, `POST` и т.д.)
     - `endpoint`: Путь API эндпоинта
     - `http_status`: HTTP-статус ответа
   - Описание: Отслеживает количество запросов к приложению.

2. **Задержка запросов** (`flask_app_request_latency_seconds`):
   - Метки:
     - `method`: HTTP-метод
     - `endpoint`: Путь API эндпоинта
   - Описание: Измеряет задержку запросов в секундах.

### Метрики по умолчанию

Клиент Prometheus автоматически экспортирует метрики уровня приложения, такие как:
- `process_cpu_seconds_total`: Использование CPU процессом.
- `process_resident_memory_bytes`: Использование памяти процессом.
- `python_gc_objects_collected_total`: Статистика сборщика мусора Python.

---

[""](images/1.png)

[""](images/2.png)

[""](images/3.png)

