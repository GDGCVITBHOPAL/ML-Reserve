from customer_personality.exception.exception_handler import AppException

from customer_personality.pipeline.training_pipeline import TrainingPipeline

obj = TrainingPipeline()
obj.start_training_pipeline()
print(" Training Completed!")