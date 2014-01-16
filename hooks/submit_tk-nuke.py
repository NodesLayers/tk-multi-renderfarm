import nuke

import tank
from tank import Hook
from tank import TankError


class PostSubmitHook(Hook):
    def execute(self, app, outputs, **kwargs):
        '''
        app:        main class app
        outputs:    list of dicts with the following keys:

                    output:     Dict
                                Dictionary with all data from the outputs:

                                name:         String
                                              Name of output in the environment.

                                tank_type:    String
                                              Tank type specified in the environment.

                    <attr1>:     String, Int or Bool

                    <attr2>:     String, Int or Bool
        '''

        self.app = app
        self.outputs = outputs

        results = []

        for output in self.outputs:
            errors = []
            if output['output']['name'] == "nuke_render":
                try:
                    self.nuke_render(output)
                except Exception, e:
                    errors.append("Submit failed - %s" % e)

            # if there is anything to report then add to result
            if len(errors) > 0:
                # add result:
                results.append({"output": output, "errors": errors})

        return results

    def nuke_render(self, output):
        '''Method for submitting to the render farm.
        '''
        pass
