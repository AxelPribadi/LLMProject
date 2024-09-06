import submitLogo from '/submit.png';

function SubmitButton({ onSubmit, isEnabled }) {
  return (
    <button className="submitButton" onClick={onSubmit} disabled={!isEnabled}>
      {/* Submit */}
      <img src={submitLogo} className="submitLogo" alt="Submit"/>
    </button>
  );
}


export default SubmitButton;
