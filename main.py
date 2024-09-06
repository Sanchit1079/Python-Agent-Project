import threading
from activity_tracker import start_activity_monitoring
from timezone_manager import monitor_timezone_changes
from status_monitor import monitor_system_status

if __name__ == "__main__":
    # Activity
    activity_thread = threading.Thread(target=start_activity_monitoring)
    activity_thread.daemon = True
    activity_thread.start()

    # Timezone
    timezone_thread = threading.Thread(target=monitor_timezone_changes)
    timezone_thread.daemon = True
    timezone_thread.start()

    # Status
    status_thread = threading.Thread(target=monitor_system_status)
    status_thread.daemon = True
    status_thread.start()

    # Main
    activity_thread.join()
    timezone_thread.join()
    status_thread.join()
