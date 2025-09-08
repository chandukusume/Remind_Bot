module.exports = {
  apps: [
    {
      name: 'rasa-server',
      script: 'rasa',
      args: 'run --enable-api --cors "*" --debug',
      cwd: '/home/pavan/Remind_Bot',
      interpreter: '/home/pavan/Remind_Bot/venv/bin/python3',
      autorestart: true,
      watch: false,
      max_memory_restart: '1G',
      env: {
        PATH: '/home/pavan/Remind_Bot/venv/bin:' + process.env.PATH,
        PYTHONPATH: '/home/pavan/Remind_Bot'
      }
    },
    {
      name: 'action-server',
      script: 'rasa',
      args: 'run actions',
      cwd: '/home/pavan/Remind_Bot',
      interpreter: '/home/pavan/Remind_Bot/venv/bin/python3',
      autorestart: true,
      watch: false,
      max_memory_restart: '1G',
      env: {
        PATH: '/home/pavan/Remind_Bot/venv/bin:' + process.env.PATH,
        PYTHONPATH: '/home/pavan/Remind_Bot'
      }
    },
    {
      name: 'telegram-bridge',
      script: 'telegram_bridge.py',
      cwd: '/home/pavan/Remind_Bot',
      interpreter: '/home/pavan/Remind_Bot/venv/bin/python3',
      autorestart: true,
      watch: false,
      max_memory_restart: '500M',
      env: {
        PATH: '/home/pavan/Remind_Bot/venv/bin:' + process.env.PATH,
        PYTHONPATH: '/home/pavan/Remind_Bot'
      }
    }
  ]
}