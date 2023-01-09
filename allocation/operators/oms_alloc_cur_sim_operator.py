from airflow.models import BaseOperator
from airflow.plugins_manager import AirflowPlugin
from airflow.utils.decorators import apply_defaults
from airflow.models import Variable
from allocation.views import count_cur_sim

class AllocCurSimCount(BaseOperator):

    @apply_defaults
    def __init__(self, department, *args, **kwargs):
        self.department = department
        super(AllocCurSimCount, self).__init__(*args, **kwargs)

    def execute(self, context):
        try:
            res = count_cur_sim()
            return res
        except Exception as e:
            print(e)