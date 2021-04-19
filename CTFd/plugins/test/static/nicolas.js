



CTFd._internal.challenge.start_vm = function (preview) {
  var challenge_id = 1
  var submission = 10

  var body = {
    'challenge_id': challenge_id,
    'submission': submission,
  }
  var params = {}
  if (preview) {
    params['preview'] = true
  }

  return CTFd.api.start_vm(params, body).then(function (response) {
    if (response.status === 429) {
      // User was ratelimited but process response
      return response
    }
    if (response.status === 403) {
      // User is not logged in or CTF is paused.
      return response
    }
    console.log(response);
    return response
  })
};
