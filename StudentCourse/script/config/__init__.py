from configparser import ConfigParser
import sys



# class EnvInterpolation(BasicInterpolation):
#     """
#     Interpolation which expands environment variables in values.
#     """

#     def before_get(self, parser, section, option, value, defaults):
#         value = super().before_get(parser, section, option, value, defaults)

#         if not os.path.expandvars(value).startswith("$"):
#             return os.path.expandvars(value)
#         else:
#             return

try:
    config = ConfigParser()
    config.read("conf/application.conf")
except Exception as e:
    print(f"Error while loading the config: {e}")
    print("Failed to Load Configuration. Exiting!!!")
    sys.stdout.flush()
    sys.exit()

class DBConf:
    MONGO_URI = config.get("MONGO_DB", "uri")
    MONGO_DBNAME=config.get("MONGO_DB","db_name")
    MONGO_COLLNAME=config.get("MONGO_DB","coll_name")
    if not MONGO_URI:
        print("Error, environment variable MONGO_URI not set")
        sys.exit(1)

class Service:
    port=int(config.get("SERVICE", "port"))
    host=config.get("SERVICE","host")



